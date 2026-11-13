"""Tests for slop_scan.py. Run: python3 -I scripts/test_slop_scan.py"""
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import slop_scan  # noqa: E402

FIX = HERE / "fixtures"


def rules_in(path, text=False):
    hits, _ = slop_scan.scan([str(path)], text)
    return {h.rule for h in hits}, hits


class UiRules(unittest.TestCase):
    def test_slop_html_hits_every_expected_rule(self):
        found, _ = rules_in(FIX / "slop.html")
        expected = {
            "hue-gradient", "css-gradient", "gradient-text", "colored-glow", "backdrop-blur",
            "heavy-weight", "tracked-caps", "emoji", "arrow-glyph", "off-grid-tw", "off-grid-css",
            "greeting", "exclamation", "wordy-placeholder", "hype-ui", "unverified-claim",
            "intro-badge", "em-dash-ui", "pill-everything", "loop-anim", "transition-all", "hover-lift",
            "stock-font", "template-copy", "fake-urgency", "placeholder-people", "fake-logos",
            "builder-fingerprint", "default-title", "recipe-fingerprint", "placeholder-asset",
            "missing-description", "missing-social-image",
        }
        self.assertEqual(expected - found, set())

    def test_clean_html_is_silent(self):
        found, hits = rules_in(FIX / "clean.html")
        self.assertEqual(found, set(), [f"{h.line} {h.rule}" for h in hits])

    def test_off_grid_math(self):
        self.assertTrue(slop_scan.off_grid("13"))
        self.assertTrue(slop_scan.off_grid("6"))
        for ok in ("1", "2", "4", "12", "16", "24", "104"):
            self.assertFalse(slop_scan.off_grid(ok), ok)

    def test_grey_gradient_is_not_hue_gradient(self):
        self.assertEqual(slop_scan.chromatic_stops("#2b2b2b, #1f1f1f"), 0)
        self.assertEqual(slop_scan.chromatic_stops("90deg, #7c3aed, #3b82f6"), 2)
        self.assertEqual(slop_scan.chromatic_stops("rgba(139, 92, 246, .5), rgb(0,0,0)"), 1)

    def test_double_negation_in_js_is_not_exclamation(self):
        hits = slop_scan.scan_text("const a = !!b && !!c;", slop_scan.UI_RULES, "x.js")
        self.assertNotIn("exclamation", {h.rule for h in hits})

    def test_css_pills_count(self):
        css = ".a{border-radius:9999px}" * 6
        hits = slop_scan.scan_text(css.replace("}", "}\n"), slop_scan.UI_RULES, "x.css")
        self.assertIn("pill-everything", {h.rule for h in hits})

    def ui(self, src):
        return {h.rule for h in slop_scan.scan_text(src, slop_scan.UI_RULES, "x.tsx")}

    def test_negative_and_axis_tailwind_values(self):
        self.assertIn("off-grid-tw", self.ui('<div className="-mt-[13px]">'))
        self.assertIn("off-grid-tw", self.ui('<div className="mx-[10px]">'))
        self.assertNotIn("off-grid-tw", self.ui('<div className="max-w-[700px] w-[375px]">'))

    def test_jsx_expressions_inside_copy(self):
        self.assertIn("exclamation", self.ui("<p>Welcome {user.name}!</p>"))
        self.assertIn("em-dash-ui", self.ui('<Button title="Fast — reliable" />'))

    def test_reversed_classes_and_other_color_spaces(self):
        self.assertIn("hue-gradient", self.ui('<div className="to-blue-500 bg-gradient-to-r from-purple-600">'))
        self.assertIn("colored-glow", self.ui('<div className="shadow-purple-500/50 shadow-md">'))
        self.assertEqual(slop_scan.chromatic_stops("hsl(270 80% 60%), oklch(0.6 0.2 250)"), 2)
        self.assertEqual(slop_scan.chromatic_stops("hsl(0 0% 20%), oklch(0.3 0 0)"), 0)

    def test_surface_and_component_rules(self):
        self.assertIn("side-border", self.ui('<div className="border-l-4 border-blue-500 rounded-lg">'))
        self.assertNotIn("side-border", self.ui('<div className="border-l border-neutral-200">'))
        self.assertIn("cream-background", self.ui("body { background: #F5F0E8; }"))
        self.assertNotIn("cream-background", self.ui("body { background: #FAFAFA; }"))
        self.assertIn("radial-glow", self.ui(".hero { background: radial-gradient(circle, rgba(139,92,246,.4), transparent 60%); }"))
        tile = '<div className="w-12 h-12 rounded-xl bg-violet-100 flex items-center justify-center">'
        self.assertIn("icon-tile", self.ui("\n".join([tile] * 3)))
        self.assertNotIn("icon-tile", self.ui(tile))

    def test_motion_and_type_rules(self):
        self.assertIn("bounce-easing", self.ui("transition: transform 300ms cubic-bezier(0.34, 1.56, 0.64, 1);"))
        self.assertNotIn("bounce-easing", self.ui("transition: opacity 200ms cubic-bezier(0.2, 0.8, 0.2, 1);"))
        self.assertIn("extreme-tracking", self.ui("h1 { letter-spacing: -0.06em; }"))
        self.assertNotIn("extreme-tracking", self.ui("h1 { letter-spacing: -0.04em; }"))
        self.assertIn("tiny-text", self.ui(".meta { font-size: 10px; }"))
        self.assertNotIn("tiny-text", self.ui(".meta { font-size: 12px; }"))

    def test_translucent_icon(self):
        hit = [
            '<path stroke="rgba(0,0,0,0.4)" d="M1 1h14"/>',
            '<path stroke-opacity="0.5" d="M1 1h14"/>',
            '<circle fill-opacity="0.4" r="4"/>',
            '<path stroke="rgb(0 0 0 / 40%)" d="M1 1h14"/>',
            '<path fill="#00000066" d="M1 1h14"/>',
        ]
        miss = [
            '<path stroke="#8a8a8a" d="M1 1h14"/>',
            '<path stroke-opacity="1" d="M1 1h14"/>',
            '<path stroke-opacity="0.99" d="M1 1h14"/>',
            '<rect fill="rgba(0,0,0,0.04)" width="9" height="9"/>',
            '<svg opacity=".4"><path stroke="#555" d="M1 1h14"/></svg>',
        ]
        for snippet in hit:
            self.assertIn("translucent-icon", self.ui(snippet), snippet)
        for snippet in miss:
            self.assertNotIn("translucent-icon", self.ui(snippet), snippet)

    def test_markup_checks(self):
        found = {h.rule for h in slop_scan.markup_checks("<h1>A</h1>\n<h3>B</h3>", "x.html")}
        self.assertIn("skipped-heading", found)
        self.assertEqual(slop_scan.markup_checks("<h1>A</h1><h2>B</h2><h3>C</h3><h2>D</h2>", "x.html"), [])
        scene = "<svg>" + "<circle r='1'/>" * 30 + "</svg>"
        self.assertIn("svg-scene", {h.rule for h in slop_scan.markup_checks(scene, "x.html")})

    def test_copy_rules(self):
        self.assertIn("aphorism", self.ui("<p>Ship faster. No meetings.</p>\n<p>Not a tool. A teammate.</p>"))
        self.assertIn("placeholder-asset", self.ui('<img alt="team">'))

    def test_one_or_two_tracked_labels_are_fine(self):
        self.assertNotIn("tracked-caps", self.ui('<span class="uppercase tracking-wide">A</span>\n<span class="uppercase tracking-wide">B</span>'))

    def test_html_with_metadata_has_no_metadata_hits(self):
        doc = '<html><head><meta name="description" content="x"><meta property="og:image" content="/a.png"></head></html>'
        self.assertEqual(slop_scan.file_checks(doc, "x.html"), [])
        self.assertEqual({h.rule for h in slop_scan.file_checks("<head></head>", "x.html")},
                         {"missing-description", "missing-social-image"})

    def test_title_with_real_name_is_fine(self):
        self.assertNotIn("default-title", self.ui("<title>Contramar · Menu</title>"))
        self.assertIn("default-title", self.ui("<title>Vite + React + TS</title>"))

    def test_plain_uppercase_without_tracking_is_fine(self):
        self.assertNotIn("tracked-caps", self.ui(".kbd { text-transform: uppercase; }"))

    def test_spanish_hype_in_ui(self):
        self.assertIn("hype-ui", self.ui("<h1>Potenciá tu negocio, impulsado por IA</h1>"))

    def test_few_pills_are_fine(self):
        hits = slop_scan.scan_text('<a class="rounded-full"></a>' * 3, slop_scan.UI_RULES, "x.html")
        self.assertNotIn("pill-everything", {h.rule for h in hits})


class TextRules(unittest.TestCase):
    def test_slop_md_hits_every_category(self):
        _, hits = rules_in(FIX / "slop.md")
        cats = {h.category for h in hits}
        self.assertEqual({"words", "openers", "contrast", "reveals", "puffery", "rhythm", "endings", "punctuation"} - cats, set())

    def test_clean_md_is_silent_and_ignores_code(self):
        found, hits = rules_in(FIX / "clean.md")
        self.assertEqual(found, set(), [f"{h.line} {h.rule}" for h in hits])

    def test_recap_reports_its_own_line(self):
        hits = slop_scan.scan_text("Point one.\n\nIn conclusion, done.", slop_scan.TEXT_RULES, "x.md")
        recap = [h for h in hits if h.rule == "recap-ending"]
        self.assertEqual([h.line for h in recap], [3])

    def test_markdown_bullets_are_not_dashes(self):
        hits = slop_scan.scan_text("- one\n- two\n", slop_scan.TEXT_RULES, "x.md")
        self.assertNotIn("em-dash", {h.rule for h in hits})

    def test_tilde_fences_and_double_backticks_are_ignored(self):
        text = "~~~\nIt's not X, it's Y — leverage\n~~~\nUse ``a ` b`` then go on.\n"
        hits = slop_scan.scan_text(slop_scan.strip_code_blocks(text), slop_scan.TEXT_RULES, "x.md")
        self.assertEqual({h.rule for h in hits}, set())

    def test_spanish_fragments(self):
        hits = slop_scan.scan_text("Así de fácil. Él lo sabe. Ésa es. Ágil. Fin.", slop_scan.TEXT_RULES, "x.md")
        self.assertIn("fragments", {h.rule for h in hits})

    def test_spanish_and_portuguese_contrast(self):
        for s in ("No es una app, es una experiencia.", "Não é um app, é uma experiência."):
            hits = slop_scan.scan_text(s, slop_scan.TEXT_RULES, "x.md")
            self.assertIn("contrast-frame", {h.rule for h in hits}, s)


class AntiwebslopCatalog(unittest.TestCase):
    """One real-code case per pattern of antiwebslop.com/patrones-de-slop that code can show."""

    def ui(self, src, name="x.html"):
        hits = slop_scan.scan_text(src, slop_scan.UI_RULES, name) + slop_scan.markup_checks(src, name)
        return {h.rule for h in hits}

    def text(self, src):
        return {h.rule for h in slop_scan.scan_text(src, slop_scan.TEXT_RULES, "x.md")}

    CASES = [
        ('<button class="btn">Empezar</button>', "dead-button"),
        ('<a href="/x">Saber más →</a>', "dead-button"),
        ('<section data-aos="fade-up">', "scroll-reveal"),
        ('<motion.div whileInView={{ opacity: 1 }}>', "scroll-reveal"),
        ('<h2>Desbloquea el poder de tus datos</h2>', "hype-ui"),
        ('<button class="bg-indigo-600 text-white">', "stock-palette"),
        ('.hero{background:#09090b;color:#a3e635}', "stock-palette"),
        ('.card:hover { transform: translateY(-4px); }', "hover-lift"),
        ('.card{border-radius:16px;border-top:4px solid #8b5cf6}', "top-border"),
        ('<p>Integra sin fricción, sin esfuerzo, sin complicaciones.</p>', "stacked-without"),
        ('<h1>La plataforma con IA para equipos modernos</h1>', "template-copy"),
        ('<h1>Productos que la gente <em>ama</em></h1>', "headline-highlight"),
        ('<button><Sparkles className="h-4 w-4" /> Generar</button>', "ai-sparkle"),
        ("import { ArrowRight, Check } from 'lucide-react'", "lucide-default"),
        ('<p>No es un software. Es un movimiento.</p>', "contrast-ui"),
        ('<p>Sin relleno. Solo resultados.</p>', "template-copy"),
        ('<p>Menos ruido. Más señal.</p>', "template-copy"),
        ('<p>Rápido. Simple. Seguro.</p>', "template-copy"),
        ('<span>[ SISTEMA_LISTO ] // v1.0.4</span>', "mono-costume"),
        ('<div class="bento-grid">', "bento"),
        ('<div class="flex md:flex-row-reverse">', "zigzag"),
        ('h1{font-family:Impact, sans-serif}', "impact-font"),
        ('<p>Más de 2.000 personas ya se sumaron</p>', "unverified-claim"),
        ('<p>4,9★ en 2.000 reseñas</p>', "unverified-claim"),
        ('<cite>Juan Pérez, CEO de Acme S.A.</cite>', "placeholder-people"),
        ('<p>¡Ups! Algo salió mal.</p>', "template-copy"),
        ('<h2>Funciones Potentes Para Equipos Modernos</h2>', "title-case"),
        ('<h3>¿Estás seguro?</h3>', "template-copy"),
        ('<h2>¿Por qué elegirnos?</h2>', "template-copy"),
        ('<div class="swiper testimonials">', "carousel"),
        ('<span>¡Solo quedan 3 lugares! Termina en 09:59</span>', "fake-urgency"),
        ('<h1>El futuro del trabajo ya está aquí</h1>', "template-copy"),
        ('<p>Haz clic en este interruptor para cambiar de modo.</p>', "instruction-copy"),
        ('<span>Actualizado hace 2 minutos · 1.284 en línea</span>', "fake-urgency"),
        ('<span>Más popular</span>', "most-popular"),
        ('<p>No hay elementos todavía.</p>', "template-copy"),
        ('<h2>Basta de teatro en las reuniones.</h2>', "template-copy"),
        ('<p class="kpi">$45,231.89</p><p>+20.1% from last month</p>', "recipe-fingerprint"),
        ('<h1>Buenas tardes, Alex 👋</h1>', "greeting"),
        ('.btn{border:3px solid #111;box-shadow:6px 6px #111}', "hard-shadow"),
        ('@property --angle { syntax: "<angle>"; }', "spinning-border"),
        ('<div class="absolute -z-10 h-72 w-72 rounded-full bg-violet-400 blur-3xl">', "blur-blob"),
        ('.photo::after{content:"";position:absolute;inset:0;background:#1e1e1ed9}', "photo-veil"),
        ('.sub{color:#d0d0d0}', "faint-hex"),
        ('<p class="text-gray-300">Nuestra plataforma ayuda</p>', "faint-text"),
        ('<Loader2 className="animate-spin" />', "spinner"),
        ('<CountUp end={10000} />', "count-up"),
        ('<div class="animate-float">', "loop-anim"),
        (".card{border:1px solid #ececec;box-shadow:0 30px 60px -10px #00000038}\n" * 3, "thin-border-wide-shadow"),
        ('.blob{background:radial-gradient(circle at 25% 30%,#c4b5fd 0,#0000 45%)}', "radial-glow"),
        ('<span class="eyebrow">NUESTRA MISIÓN</span><h2>Nuestra misión es simple</h2>', "label-repeats-heading"),
        ('<span>FUNCIONES</span><span>PRECIOS</span><span>EQUIPO</span>', "caps-label"),
        ('<p>5 min de lectura · Diseño · 2026</p><p>Abril · Blog · Notas</p>', "dot-facts"),
        ('<div class="kbd">Rápido</div><div>Seguro</div><div>Simple</div>', "generic-benefit"),
        ('<details>a</details><details>b</details><details>c</details>', "faq-accordion"),
    ]

    def test_every_catalog_case(self):
        missed = [(src, rule) for src, rule in self.CASES if rule not in self.ui(src)]
        self.assertEqual(missed, [])

    def test_newsletter_and_required_forms(self):
        form = '<form>' + ''.join(f'<input name="f{i}" required>' for i in range(6)) + '<button>Suscribirme</button></form>'
        found = self.ui(form)
        self.assertIn("long-newsletter-form", found)
        self.assertIn("all-required", found)
        ok = '<form><input type="email" name="email" required><button>Suscribirme</button></form>'
        self.assertEqual(self.ui(ok) & {"long-newsletter-form", "all-required"}, set())

    def test_count_rules_work_on_minified_html(self):
        one_line = '<a class="rounded-full"></a>' * 6
        self.assertIn("pill-everything", self.ui(one_line))

    def test_spanish_contrast_in_writing(self):
        for s in ("Lo peor no era el diseño. Eran los textos.", "No es solo para webs.",
                  "No se trata de velocidad, se trata de foco."):
            self.assertIn("contrast-frame", self.text(s), s)
        self.assertIn("stacked-without", self.text("Sin fricción, sin esfuerzo."))

    def test_false_positives_stay_quiet(self):
        quiet = [
            ('<button>Reservar mesa</button>', "dead-button"),
            ('<h1>Every task has an owner and a date.</h1>', "title-case"),
            ('<h2>Cómo funciona Taskflow</h2>', "title-case"),
            ('.card{border-top:1px solid #eee}', "top-border"),
            ('.btn{box-shadow:0 4px 12px rgba(0,0,0,.1)}', "hard-shadow"),
            ('.t{color:#57534c}', "faint-hex"),
            ('<p>Seguro</p>', "generic-benefit"),
            ('<span>FAQ</span>', "caps-label"),
            ('<p>Mayo · 2026</p>', "dot-facts"),
            ('<p>Sin tarjeta de crédito.</p>', "stacked-without"),
        ]
        loud = [(src, rule) for src, rule in quiet if rule in self.ui(src)]
        self.assertEqual(loud, [])


class Cli(unittest.TestCase):
    def test_exit_codes(self):
        self.assertEqual(slop_scan.main([str(FIX / "clean.html")]), 0)
        self.assertEqual(slop_scan.main([str(FIX / "slop.md")]), 1)
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(slop_scan.main([d]), 2)

    def test_text_flag_applies_writing_rules(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "post.html"
            p.write_text("In today's world we leverage synergy.", encoding="utf-8")
            found, _ = rules_in(p, text=True)
            self.assertIn("inflated-word", found)


if __name__ == "__main__":
    unittest.main(verbosity=1)

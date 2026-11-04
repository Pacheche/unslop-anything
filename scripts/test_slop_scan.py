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

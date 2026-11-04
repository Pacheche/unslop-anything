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

"""Smoke test for the GRØNN fork: the scripts run on Dutch and keep the house rules.

    python3 tests/test_nl.py
"""
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "tests")


def run(script, *args, stdin=None):
    p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "skills", script), *args],
                       input=stdin, capture_output=True, text=True)
    return p.returncode, p.stdout


class DutchHooks(unittest.TestCase):
    def test_ranking(self):
        _, out = run("ig-reel/hookscore.py", os.path.join(HERE, "hooks-nl.txt"), "--json")
        score = {r["hook"]: r for r in json.loads(out)}
        self.assertEqual(score["Je vijver kleurt groen door één fout in maart."]["verdict"], "STRONG")
        self.assertEqual(score["Drie planten die je vijver gratis schoon houden."]["verdict"], "STRONG")
        for weak in ["Hoi allemaal, vandaag laat ik jullie mijn tuin zien!",
                     "In deze video laat ik zien hoe je een vijver aanlegt.",
                     "#vijver Zo maak je een vijver"]:
            self.assertEqual(score[weak]["verdict"], "WEAK")
            self.assertTrue(score[weak]["flags"])

    def test_english_still_works(self):
        _, out = run("ig-reel/hookscore.py", "--hook", "I lost $18,000 on one missing contract.", "--json")
        self.assertEqual(json.loads(out)["verdict"], "STRONG")

    def test_beats(self):
        code, out = run("ig-reel/beats.py", os.path.join(HERE, "script-nl.txt"), "--json")
        self.assertEqual(json.loads(out)["total_words"], 67)


class DutchCaption(unittest.TestCase):
    def test_good_caption_ready(self):
        code, out = run("ig-caption/caption.py", os.path.join(HERE, "caption-nl.txt"), "--json")
        self.assertEqual(json.loads(out)["verdict"], "READY")

    def test_house_rules(self):
        code, out = run("ig-caption/caption.py", "-", "--json",
                        stdin="Mooie vijver in Stein 🌿🌿 Stuur een foto.\n#vijver\n")
        checks = {c["check"]: c["status"] for c in json.loads(out)["checks"]}
        self.assertEqual(checks["HASHTAGS"], "FAIL")
        self.assertEqual(checks["EMOJI TWICE"], "FAIL")
        self.assertEqual(checks["DIENST + PLAATS"], "PASS")


class DutchHumanizer(unittest.TestCase):
    def test_slop_replaced(self):
        _, out = run("ig-human/humanize.py", "-",
                     stdin="Wij creëren een groene oase. Bovendien ontzorgen wij je.\n")
        self.assertIn("maken een tuin", out)
        self.assertNotIn("ontzorgen", out)

    def test_dutch_voice_not_punished(self):
        _, out = run("ig-human/detect.py", os.path.join(HERE, "caption-nl.txt"), "--json")
        self.assertGreaterEqual(json.loads(out)["checks"]["VOICE"]["score"], 90)


if __name__ == "__main__":
    unittest.main()

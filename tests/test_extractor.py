import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from speech_to_graph.extractor import SpeechToGraphExtractor

class TestSpeechToGraph(unittest.TestCase):
    def test_extraction(self):
        ext = SpeechToGraphExtractor()
        text = "Meeting transcript:\nJohn: We need to finalize the deployment.\nMary: Done."
        items = ext.extract_action_items(text)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["trigger"], "need to")

if __name__ == "__main__":
    unittest.main()

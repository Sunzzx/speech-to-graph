"""Speech to Action Graph Semantic Extractor."""
import re
from typing import List, Dict, Any

class SpeechToGraphExtractor:
    def __init__(self):
        self.triggers = ["action item", "todo", "need to", "will deploy", "assign to"]

    def extract_action_items(self, transcript: str) -> List[Dict[str, Any]]:
        actions = []
        lines = transcript.splitlines()
        for i, line in enumerate(lines):
            clean = line.strip()
            for trig in self.triggers:
                if trig in clean.lower():
                    actions.append({"id": f"task-{i}", "raw": clean, "trigger": trig})
                    break
        return actions

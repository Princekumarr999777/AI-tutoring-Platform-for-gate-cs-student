from pathlib import Path
CASES = [("What is a binary search tree?", "algorithms/bst.pdf"), ("What does an index do?", "dbms/index.pdf")]
if __name__ == "__main__":
    lines = ["# RAG Evaluation Report", "", "Offline fixture mode; live model/retrieval scores are unavailable.", "", "| Question | Expected source |", "|---|---|"]
    lines.extend(f"| {question} | `{source}` |" for question, source in CASES)
    Path("docs/evaluation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

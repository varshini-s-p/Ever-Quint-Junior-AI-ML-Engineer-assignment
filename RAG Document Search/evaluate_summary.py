from rouge_score import rouge_scorer
from rag_pipeline import summarize_documents, initialize_store
from utils import extract_text, chunk_text

DOCUMENT_PATH = "data/uploads/Artificial_intelligence.pdf"  # adjust if needed

def setup_index():
    text = extract_text(DOCUMENT_PATH)
    chunks = chunk_text(text)
    initialize_store(chunks)

def evaluate_summary():
    reference_summary = """
    Artificial Intelligence focuses on building systems that can perform tasks
    such as learning, reasoning, and perception. Machine learning enables systems
    to improve from data, while neural networks model complex patterns.
    """

    generated_summary = summarize_documents("medium")

    scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
    scores = scorer.score(reference_summary, generated_summary)

    print("ROUGE-1 F1:", round(scores["rouge1"].fmeasure, 3))
    print("ROUGE-L F1:", round(scores["rougeL"].fmeasure, 3))

if __name__ == "__main__":
    setup_index()
    evaluate_summary()

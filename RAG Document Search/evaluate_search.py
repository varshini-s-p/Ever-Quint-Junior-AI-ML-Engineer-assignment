from utils import extract_text, chunk_text
from rag_pipeline import initialize_store, hybrid_search
from evaluation_data import TEST_QUERIES

DOCUMENT_PATH = "data/uploads/Artificial_intelligence.pdf"

def evaluate_search(top_k=5):
    hits = 0

    for item in TEST_QUERIES:
        results = hybrid_search(item["query"], top_k=top_k)
        combined_text = " ".join(results).lower()

        if item["expected_keyword"] in combined_text:
            hits += 1

    accuracy = hits / len(TEST_QUERIES)
    print(f"Search Hit@{top_k}: {accuracy:.2f}")


if __name__ == "__main__":
    # ---- INITIALIZE STORE FOR EVALUATION ----
    text = extract_text(DOCUMENT_PATH)
    chunks = chunk_text(text)
    initialize_store(chunks)

    # ---- RUN EVALUATION ----
    evaluate_search()

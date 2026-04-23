from llm import generate_answer

def classify(query: str):
    q = query.lower()

    if "refund" in q:
        return "refund"
    if "return" in q:
        return "return"
    if "cancel" in q:
        return "cancel"
    if "cod" in q or "cash on delivery" in q:
        return "payment"
    if "human" in q or "angry" in q:
        return "escalate"

    return "general"


def retrieve(db, query):
    # 🔥 IMPROVED RETRIEVAL (TOP-K + SCORE ORDERED)
    docs = db.similarity_search_with_score(query, k=3)

    chunks = []

    for doc, score in docs:
        chunks.append({
            "text": doc.page_content,
            "score": float(score)
        })

    # sort best match first (VERY IMPORTANT FIX)
    chunks = sorted(chunks, key=lambda x: x["score"])

    return chunks


def build_graph(db):

    def workflow(state):

        query = state["query"]

        intent = classify(query)

        chunks = retrieve(db, query)

        escalate = intent == "escalate"

        answer = generate_answer(query, chunks)

        return {
            "query": query,
            "intent": intent,
            "chunks": chunks,
            "answer": answer,
            "score": 1.0,
            "escalate": escalate
        }

    return workflow

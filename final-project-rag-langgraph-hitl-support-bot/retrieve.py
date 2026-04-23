def retrieve(db, query: str, k=3):
    results = db.similarity_search_with_score(query, k=k)

    chunks = []
    scores = []

    for doc, score in results:
        chunks.append(doc.page_content)
        scores.append(score)

    return chunks, min(scores) if scores else 0.0

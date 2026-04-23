def generate_answer(query, chunks):

    def get_text(c):
        return c["text"] if isinstance(c, dict) else str(c)

    context = [get_text(c) for c in chunks]

    query_words = query.lower().split()

    best_sentence = ""
    best_score = 0

    for chunk in context:
        sentences = chunk.split(".")

        for sentence in sentences:
            clean = sentence.strip()

            # remove FAQ labels like Q1, Q2, Q5
            clean = clean.replace("Q1:", "").replace("Q2:", "").replace("Q3:", "").replace("Q4:", "").replace("Q5:", "").strip()

            score = sum(1 for w in query_words if w in clean.lower())

            if score > best_score:
                best_score = score
                best_sentence = clean

    if not best_sentence:
        best_sentence = context[0] if context else "No answer found"

    # FINAL CLEAN OUTPUT
    return f"""
📌 FINAL ANSWER:

{best_sentence}

👉 (Extracted via RAG + scoring + cleanup)
"""

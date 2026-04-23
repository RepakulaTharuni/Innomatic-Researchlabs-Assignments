def should_escalate(score: float, query: str):

    if score < 0.3:
        return True

    low_confidence_keywords = [
        "angry", "frustrated", "cancel everything", "human", "agent"
    ]

    if any(word in query.lower() for word in low_confidence_keywords):
        return True

    return False

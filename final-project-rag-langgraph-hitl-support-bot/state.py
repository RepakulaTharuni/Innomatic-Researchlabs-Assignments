from typing import TypedDict, List, Dict, Any

class GraphState(TypedDict):
    query: str
    intent: str
    chunks: List[Dict]
    answer: str
    score: float
    escalate: bool

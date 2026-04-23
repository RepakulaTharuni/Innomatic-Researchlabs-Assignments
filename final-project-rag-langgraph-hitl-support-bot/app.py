from ingest import create_vector_db
from graph import build_graph

def main():

    print("🚀 RAG + HITL SYSTEM STARTED")

    pdf_path = "sample.pdf"

    # INIT DB
    db = create_vector_db(pdf_path)

    # BUILD GRAPH
    app = build_graph(db)

    # CHAT LOOP
    while True:

        query = input("\n💬 Ask question (type exit): ")

        if query.lower() == "exit":
            break

        state = {
            "query": query,
            "intent": "",
            "chunks": [],
            "answer": "",
            "score": 0,
            "escalate": False
        }

        result = app(state)

        print("\n🤖 ANSWER:\n")
        print(result["answer"])
        print("\n" + "-" * 60)


if __name__ == "__main__":
    main()

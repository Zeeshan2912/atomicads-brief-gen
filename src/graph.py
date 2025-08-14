from langgraph.graph import StateGraph

def mock_final_brief(state):
    return {
        "final_brief": {
            "topic": state["topic"],
            "depth": state["depth"],
            "summary": f"This is a mock summary for topic '{state['topic']}' with depth {state['depth']}.",
            "key_findings": ["Finding 1", "Finding 2", "Finding 3"],
            "sources": [
                {"title": "Mock Source 1", "url": "http://example.com", "snippet": "Snippet about the topic."},
                {"title": "Mock Source 2", "url": "http://example.com", "snippet": "Another snippet."}
            ],
            "plan": ["Step 1: Research", "Step 2: Summarize", "Step 3: Validate"],
            "metadata": {"tokens_used": 500},
            "generated_at": "2025-08-13T15:30:00Z"
        }
    }

graph = StateGraph(dict)
graph.add_node("final_brief", mock_final_brief)
graph.set_entry_point("final_brief")

from core.state import LayoutState
from langgraph.graph import StateGraph, END

class LayoutOrchestrator:
    def __init__(self):
        self.builder = StateGraph(LayoutState)

    def build_layout_graph(self):
        self.builder.add_node("layout", self._layout_agent().handle_state)
        self.builder.set_entry_point("layout")
        self.builder.add_edge("layout", END)
        return self.builder.compile()

    def _layout_agent(self):
        from agents.layout_agent import LayoutAgent
        return LayoutAgent()


if __name__ == "__main__":
    obj = LayoutOrchestrator().build_layout_graph()
    user_prompt = input("Describe your layout: ")
    initial_state = {"user_prompt": user_prompt}
    result = obj.invoke(initial_state)
    print("\n🧠 Layout Suggestion:")
    print(result["layout_response"])


    
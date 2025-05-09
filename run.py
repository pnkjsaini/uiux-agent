# run.py

from core.orchestrator import LayoutOrchestrator


class LayoutRunner:
    def __init__(self):
        self.graph = LayoutOrchestrator().build_layout_graph()

    def run(self):
        user_prompt = input("Describe your layout: ")
        initial_state = {"user_prompt": user_prompt}
        result = self.graph.invoke(initial_state)
        print("\n🧠 Layout Suggestion:")
        print(result["layout_response"])


if __name__ == "__main__":
    runner = LayoutRunner()
    runner.run()

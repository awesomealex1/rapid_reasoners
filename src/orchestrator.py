from agents.planner import PlannerAgent
from agents.developer import DeveloperAgent
from agents.reviewer import ReviewerAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.developer = DeveloperAgent()
        self.reviewer = ReviewerAgent()

    def orchestrate(self, input_data):
        plan = self.planner.execute(input_data)
        data_analysis = self.developer.execute(plan)
        review_result = self.reviewer.execute(data_analysis)

        iteration = 0

        max_iterations = 10

        while iteration < max_iterations:
            if review_result["status"] == "valid":
                print("Result validated:", review_result["result"])
                return review_result["result"]
            else:
                print("Result invalid, re-executing the plan")
                plan = self.planner.execute(input_data)
                data_analysis = self.developer.execute(plan)
                review_result = self.reviewer.execute(data_analysis)
            iteration += 1

            print("Max iterations reached, returning best attempt")
            return review_result["result"]

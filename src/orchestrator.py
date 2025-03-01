from agents.planner import Planner
from agents.developer import Developer
from agents.reviewer import Reviewer
from agents.data_collector import DataCollector


class Orchestrator:
    def __init__(self):
        self.planner = Planner()
        self.data_collector = DataCollector()
        self.developer = Developer()
        self.reviewer = Reviewer()

    def orchestrate(self, input_data):
        plan = str(self.planner.execute(input_data))
        data = str(self.data_collector.execute(plan))
        data_analysis = str(self.developer.execute(data))
        review_result = str(self.reviewer.execute(data_analysis))

        iteration = 0

        max_iterations = 10

        while iteration < max_iterations:
            if "yes" in review_result:
                return review_result
            else:
                print("Result invalid, re-executing the plan")
                plan = str(self.planner.execute(input_data))
                data = str(self.data_collector.execute(plan))
                data_analysis = str(self.developer.execute(data))
                review_result = str(self.reviewer.execute(data_analysis))
            iteration += 1

        print("Max iterations reached, returning best attempt")
        return review_result

from agents.planner import Planner
from agents.developer import Developer
from agents.reviewer import Reviewer
#from agents.presenter import Presenter
from agents.data_collector import DataCollector
from agents.find_consumer_products import ProductDeveloper

class Orchestrator:
    def __init__(self):
        self.planner = Planner()
        self.data_collector = DataCollector()
        self.developer = Developer()
        #self.presenter = Presenter()
        self.reviewer = Reviewer()
        self.product = ProductDeveloper()

    def orchestrate(self, input_data):
        plan = str(self.planner.execute(input_data))
        tik_tok_labels = str(self.data_collector.execute(plan))
        raw_consumer_data = str(self.developer.execute(tik_tok_labels))
        consumer_products = str(self.product.execute(raw_consumer_data))
        #presentation = str(self.presenter.execute(consumer_products))
        review_result = str(self.reviewer.execute(consumer_products))

        iteration = 0

        max_iterations = 10

        while iteration < max_iterations:
            if "yes" in review_result:
                return review_result
            else:
                print("Result invalid, re-executing the plan")
                plan = str(self.planner.execute(input_data))
                tik_tok_labels = str(self.data_collector.execute(plan))
                raw_consumer_data = str(self.developer.execute(tik_tok_labels))
                consumer_products = str(self.product.execute(raw_consumer_data))
                #presentation = str(self.presenter.execute(consumer_products))
                review_result = str(self.reviewer.execute(consumer_products))
            iteration += 1

        print("Max iterations reached, returning best attempt")
        return review_result

from agents.planner import Planner
from agents.developer import Developer
from agents.reviewer import Reviewer
#from agents.presenter import Presenter
from agents.data_collector import DataCollector
from agents.find_consumer_products import ProductDeveloper
from agents.supply_chain import SupplyChain
from agents.stock_agent import StockPicker

class Orchestrator:
    def __init__(self):
        self.planner = Planner()
        self.data_collector = DataCollector()
        self.developer = Developer()
        #self.presenter = Presenter()
        self.reviewer = Reviewer()
        self.product = ProductDeveloper()
        self.supply_chain = SupplyChain()
        self.stocks = StockPicker()

    def orchestrate(self, input_data):
        plan = str(self.planner.execute(input_data))
        tik_tok_labels = str(self.data_collector.execute(plan))
        raw_consumer_data = str(self.developer.execute(tik_tok_labels))
        consumer_products = str(self.product.execute(raw_consumer_data))
        supply_chain = str(self.supply_chain.execute(consumer_products))
        stocks = str(self.stocks.execute(supply_chain))
        review = str(self.reviewer.execute(stocks))

        iteration = 0

        max_iterations = 15

        while iteration < max_iterations:
            if "yes" in review_result:
                supply_chain = str(self.supply_chain.execute(review_result))
                return supply_chain
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

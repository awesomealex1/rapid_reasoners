from base_agent import BaseAgent

class Presenter(BaseAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_prompt = "You are the presenter agent. You need to generate stock price predictions based on the signals provided by the interpreter agent."

    def execute(self, signals, **kwargs):
        prompt = self.base_prompt + "\nThese are the signals you have been given: <SIGNALS>\n" + signals + "<\SIGNALS>\nNow generate a set of stock price predictions based on these signals."
        self.run(prompt)
        
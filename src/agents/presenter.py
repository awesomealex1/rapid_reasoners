from base_agent import BaseAgent

class Presenter(BaseAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_prompt = "You are the presenter agent. You need to generate a final report based on data given to you by the developer agent.."

    def execute(self, signals, **kwargs):
        prompt = self.base_prompt + "\nThese are the signals you have been given: <CONTEXT>\n" + signals + "<\CONTEXT>\nNow generate a report from these signals."
        self.run(prompt)
        
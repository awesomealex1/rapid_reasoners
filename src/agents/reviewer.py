from base_agent import BaseAgent

class Reviewer(BaseAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_prompt = "You are the reviewer agent. You need to review the final output given to you by a presenter agent. You need to decide whether it is good or not, by outputting \"yes\" or \"no\". A good final output contains a prediction and an explanation for the prediction."
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow decide whether this is a good final presentation or not. Output \"yes\" or \"no\"."
        self.run(prompt)

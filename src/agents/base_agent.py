from smolagents.agents import MultiStepAgent

class BaseAgent(MultiStepAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(input, **kwargs):
        raise NotImplementedError("Need to implement execute method.")
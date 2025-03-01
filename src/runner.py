from orchestrator import Orchestrator
import os

def main():
    with os.open("prompt.txt", "r") as f:
        prompt = f.readline()
    orchestrator = Orchestrator()
    result = orchestrator.orchestrate(input_data=prompt)
    print(result)

if __name__ == "__main__":
    main()
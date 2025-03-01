import os
import sys
sys.path.append(os.curdir)
from orchestrator import Orchestrator

def main():
    with open("prompt.txt", "r") as f:
        prompt = f.readline()
    orchestrator = Orchestrator()
    result = orchestrator.orchestrate(input_data=prompt)
    print(result)

if __name__ == "__main__":
    main()
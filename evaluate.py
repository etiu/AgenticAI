from evals import EVAL_CASES
from agent import ask_model
import pandas as pd
import math 



def parse_values(tool_values: dict[str, list[float]], expected_values:dict[str, list[float]]) -> bool:
    for k, v in expected_values.items(): #{"tpsa": [20.23], "pic50": [8.60]}
        found = tool_values.get(k, []) #.get is going to get the value of that key, k. [] is a backup default value if k is not in tool_values
        for val in v:
            if not any(math.isclose(t, val, abs_tol = 0.015) for t in found):
                return False
    return True
    

def main(EVAL_CASES:list)-> pd.DataFrame:
    rows = []
    for case in EVAL_CASES:
        text, tools_called, tool_values = ask_model(case['question'])
        row = {
            "Question": case['question'],
            "Response": text,
            "Tools": tools_called,
            "Pass_tools_called?": sorted(tools_called) == sorted(case['expected_tools']),
            "Pass_values?": parse_values(tool_values, case['expected_values'])
            }
        rows.append(row)
    df = pd.DataFrame(rows)
    return df


if __name__ == "__main__":
    df = main(EVAL_CASES)
    df.to_csv("eval_results.csv", index=False)


        
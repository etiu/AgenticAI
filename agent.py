import anthropic
from dotenv import load_dotenv
from tools import calc_properties, to_pic50
import json

load_dotenv() #copies the .env contents into the environment first, and the client then finds the key there.


CALC_PROPERTIES_TOOL = {
    "name": "calc_properties",
    "description": "This is a tool which calculates different properties, specifically mol weight, LogP, TPSA, number of hydrogen bond donors, number of hydrogen bond acceptors. Always use this tool for property values; never calculate them by hand or from memory. The input is always a SMILES string: 'CO' means methanol, not carbon monoxide.",
    "input_schema": {
        "type": "object",
        "properties": {
            "smiles": {
            "type": "string",
            "description": "The SMILES string of a single molecule, exactly as given by the user",
        },
    },
            "required": ['smiles'], 
    },
}

TO_PIC50_TOOL={
    "name": "to_pic50",
    "description": "a tool to convert ic50 to pic50. user input ic50 in either nM, mM, uM, or pM. the tool returns the pic50 value. If the user does not give units, do not call this tool and do not assume a unit; ask the user which unit they mean. If the user gives 0 or negative value, do not call this tool and explain to the user why.",
    "input_schema": {
        "type": "object",
        "properties": {
            "value": {
                "type": "number",
                "description": "the value to convert as inputted by user"},
            "units": {
                "type": "string",
                "description": "the unit the tool is converting from as inputted by the user.",
                "enum": ['pM', 'nM', 'uM', 'mM']
        },},
        "required": ['value', 'units']

    }
}

def run_tool(name:str, tool_input:dict) -> float | dict:
    if name == CALC_PROPERTIES_TOOL['name']:
        return calc_properties(tool_input['smiles'])
    if name == TO_PIC50_TOOL['name']:
        return to_pic50(tool_input['value'], tool_input['units'])
    return {"error": f"Unknown tool: {name!r}"}


MAX_ROUNDS = 10
def ask_model(question:str) -> tuple[str, list[str], dict[str, list[float]]]:
    tools_called =[]
    tool_results =[]
    tool_values = {}
    client = anthropic.Anthropic()          # reads the key from the environment
    messages = [
        {"role": "user", "content": question}
    ]
    response = client.messages.create(
        model="claude-haiku-5-5",           # the fastest, cheapest model; fine for learning
        max_tokens=500,
        messages=messages,
        tools = [CALC_PROPERTIES_TOOL, TO_PIC50_TOOL]
    )
    rounds = 0
    while response.stop_reason == "tool_use":
        rounds +=1
        if rounds > MAX_ROUNDS:
            return "Stopped: too many tool calls.", tools_called
        messages.append({"role": "assistant", "content": response.content}) #what you send to the model on the next call

        
        for k in response.content:
            if k.type == "tool_use":
                tools_called.append(k.name)
                result = run_tool(k.name, k.input)
                    # NEW: keep every number the tool produced
                if isinstance(result, (int, float)):        # to_pic50 returns a number
                    if "pic50" not in tool_values:
                        tool_values['pic50'] = []
                    tool_values['pic50'].append(result)#dict of lists
                elif "error" not in result:                 # calc_properties returns a dict
                    for name, v in result.items():
                        if isinstance(v, (int, float)):
                            if name not in tool_values:
                                tool_values[name] = []
                            tool_values[name].append(v)
                tool_results.append({"type": "tool_result",
                                     "tool_use_id": k.id,
                                     "content": json.dumps(result)})
        messages.append({"role": "user", 
                        "content": tool_results,
                })
        response = client.messages.create(
                model="claude-haiku-5-5",           # the fastest, cheapest model; fine for learning
                max_tokens=500,
                messages=messages,
                tools = [CALC_PROPERTIES_TOOL, TO_PIC50_TOOL]
                    )
        
    for k in response.content:
        if k.type == "text":
            return k.text, tools_called, tool_values


if __name__ == "__main__":
    answer, tools, values = ask_model("What is the pIC50 of 250 nM?")
    print(answer)
    print(tools)          # should print ['to_pic50']
    print(values)
# if __name__ == "__main__":
#     print(ask_model("What is the capital of France?"))
#     print(ask_model("What are the molecular weight and TPSA of Cc1nc(N2CCN(C(=O)C3CC3)CC2)sc1C(=O)Nc1ccc(F)cc1?"))
#     print(ask_model("Which has the higher TPSA: CCO or c1ccccc1O?"))
#     print(ask_model("What is the pIC50 of 250 nM?"))
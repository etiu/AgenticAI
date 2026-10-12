import anthropic
from dotenv import load_dotenv

load_dotenv()


CALC_PROPERTIES_TOOL = {
    "name": "calc_properties",
    "description": "This is a tool which calculates different properties, specifically mol weight, LogP, TPSA, number of hydrogen bond donors, number of hydrogen bond acceptors",
    "input_schema": {
        "type": "object",
        "properties": {
            "smiles": {
            "type": "string",
            "description": "A SMILES string is a 2D representation of a molecule",
        },
    },
            "required": ['smiles'], 
    },
}
def ask_model(question:str) -> dict:
    client = anthropic.Anthropic()          # reads the key from the environment

    response = client.messages.create(
        model="claude-haiku-5-5",           # the fastest, cheapest model; fine for learning
        max_tokens=500,
        messages=[{"role": "user", "content": question}],
        tools = [CALC_PROPERTIES_TOOL]
    )

    print("stop_reason:", response.stop_reason)
    for block in response.content:
        print("block type:", block.type)
        if block.type == "tool_use":
            print("tool:", block.name)
            print("input:", block.input)
            print("id:", block.id)
    return response

ask_model("What are the molecular weight and TPSA of Cc1nc(N2CCN(C(=O)C3CC3)CC2)sc1C(=O)Nc1ccc(F)cc1?")
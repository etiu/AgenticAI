import anthropic
from anthropic.types import Message
from dotenv import load_dotenv

load_dotenv() #copies the .env contents into the environment first, and the client then finds the key there.


CALC_PROPERTIES_TOOL = {
    "name": "calc_properties",
    "description": "This is a tool which calculates different properties, specifically mol weight, LogP, TPSA, number of hydrogen bond donors, number of hydrogen bond acceptors",
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


def ask_model(question:str) -> Message:
    client = anthropic.Anthropic()          # reads the key from the environment

    response = client.messages.create(
        model="claude-haiku-5-5",           # the fastest, cheapest model; fine for learning
        max_tokens=500,
        messages=[{"role": "user", "content": question}],
        tools = [CALC_PROPERTIES_TOOL]
    )

    return response

if __name__ == "__main__":
    print(ask_model("What is the capital of France?"))
    print(ask_model("What are the molecular weight and TPSA of Cc1nc(N2CCN(C(=O)C3CC3)CC2)sc1C(=O)Nc1ccc(F)cc1?"))
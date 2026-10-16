# Molecular Property Agent (work in progress)

#### What it is?

This is a simple agentic AI tool which can use 2 functions. The agent (Claude Haiku 5.5 via the Anthropic API) uses these two: One is to calculate properties like HBD, HBA, MW, TPSA, clogP. The other tool is to convert IC50 in nM, mM, pM, or uM to pIC50. The functions can be found in tools.py.

#### Does it work?
The agent loop is written by hand, without an agent framework.
I evaluated the agent with evals.py and evaluate.py. Based on tests it score 18/19 on the correct tools called and used and it score 18/19 on correct values returned.

#### How to run it?


##### Setup

```bash
pip install anthropic python-dotenv rdkit pandas pytest
```

Create a `.env` file with `ANTHROPIC_API_KEY=your-key`, then:

```bash
python agent.py        # try the agent
python evaluate.py     # run the evaluation (saves eval_results.csv)
python -m pytest       # unit tests for the tools
```

##### Project structure

```
agent.py            agent loop and tool definitions
tools.py            calc_properties and to_pic50
evals.py            evaluation cases
evaluate.py         runs the evals and scores them
tests/              unit tests
```
#### What did I learn?

By doing this short project I learned how agenticAI's work and how they are built.

##### Findings

- **SMILES vs formula ambiguity.** The model read "CO" as carbon monoxide instead of
  the SMILES for methanol, rewrote the input, and reported 28.01 instead of 32.04.
  I added to the tool description that the input is always a SMILES string, but the
  case still fails in some runs (passed 1 of 4 so far). Next, I want to try a system
  prompt that applies to every question, and measure pass rates over repeated runs.
- **Silent unit guessing.** With no units given, the model assumed nM. I instructed it to ask instead; it now asks for the unit.
- **Untraceable numbers.** Some answers (e.g. HBD of ethanol) came from the model's
  memory rather than the tool. Values are now scored only if a tool produced them.
- **The eval set needed correcting too.** Three expectations were wrong: the agent
  behaved better than I predicted (e.g. asking for a SMILES for "xyz1234").
- **Run-to-run variation.** The same question can pass in one run and fail in the next,
  so a single run is not enough to confirm a fix.

##### Limitations

- Results are from single runs; pass rates over repeated runs would be more reliable.
- Value checks match numbers from tool outputs, not the final text, so a correct
  calculation misreported in the answer would not be caught.
- 19 cases is a small eval set.


#### Next steps
In future versions I will dockerize this so that it can be easily deployed by users. 

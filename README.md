# Molecular Property Agent (work in progress)

#### What is it?

This is a simple agentic AI tool which can use 2 functions. The agent (Claude Haiku 5.5 via the Anthropic API) uses these two: One is to calculate properties like HBD, HBA, MW, TPSA, clogP. The other tool is to convert IC50 in nM, mM, pM, or uM to pIC50. The functions can be found in tools.py.

#### Does it work?

Each of the 19 eval questions was run 3 times, and the pass rate recorded
(see `rates_results.csv`).

17 of 19 questions passed 3/3 on both checks. The exceptions: "Mw of CO"
(values 0/3) and "molecular formula of aspirin" (tools 1/3).


#### Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file with `ANTHROPIC_API_KEY=your-key`, then:

```bash
python agent.py        # try the agent
python evaluate.py     # run the evaluation (saves eval_results.csv)
python -m pytest       # unit tests for the tools
```

#### Project structure

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

- - **SMILES vs formula ambiguity.** The model read "CO" as carbon monoxide instead of
  the SMILES for methanol, rewrote the input, and reported 28.01 instead of 32.04.
  Adding "the input is always a SMILES string" to the tool description did not fix
  it: the case failed in 3 of 3 runs, so it is a systematic problem, not chance.
  Results are from 3 loop runs. pass rates over 3 runs is shown in rates_results to see how often the agent gets the tools and answers correctly.
- **Silent unit guessing.** With no units given, the model assumed nM. I instructed it to ask instead; it now asks for the unit.
- **Untraceable numbers.** Some answers (e.g. HBD of ethanol) came from the model's
  memory rather than the tool. Values are now scored only if a tool produced them.
- **The eval set needed correcting too.** Three expectations were wrong: the agent
  behaved better than I predicted (e.g. asking for a SMILES for "xyz1234").
- **Run-to-run variation.** Pass rates over 3 runs instead of single result is reported.

##### Limitations

- Value checks match numbers from tool outputs, not the final text, so a correct
  calculation misreported in the answer would not be caught.
- 19 cases is a small eval set.


#### Next steps
In future versions I will dockerize this so that it can be easily deployed by users. 

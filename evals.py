EVAL_CASES = [
    # --- pIC50 questions ---
    {
        "question": "What is the pIC50 of 250 nM?",
        "expected_tools": ["to_pic50"],
        "expected_values": {"pic50": [6.60]},
    },
    {
        "question": "What is the pIC50 of 0.25 micromolar?",
        "expected_tools": ["to_pic50"],
        "expected_values": {"pic50": [6.60]},
    },
    {
        "question": "What is the pIC50 of 250 pM?",
        "expected_tools": ["to_pic50"],
        "expected_values": {"pic50": [9.60]},
    },
    {
        "question": "What is the pIC50 of 2.5 M?",
        "expected_tools": ["to_pic50"],
        "expected_values": {"pic50": [-0.40]},
    },
    # --- property questions ---
    {
        "question": "What is the TPSA of CCO?",
        "expected_tools": ["calc_properties"],
        "expected_values": {"tpsa": [20.23]},
    },
    {
        "question": "What is the mol weight of CCO?",
        "expected_tools": ["calc_properties"],
        "expected_values": {"mol_weight": [46.07]},
    },
    {
        "question": "What is the Mw of CO?",
        "expected_tools": ["calc_properties"],
        "expected_values": {"mol_weight": [32.04]},
    },
    {
        "question": "What is the Mw of CH4O?",
        "expected_tools": ["calc_properties"],
        "expected_values": {"mol_weight": [32.04]},
    },
    {
        "question": "How many HBD are there in CCO?",
        "expected_tools": ["calc_properties"],
        "expected_values": {"hbd": [1]},
    },
    {
        "question": "What is the Hydrog bond acceptor count of CCO?",
        "expected_tools": ["calc_properties"],
        "expected_values": {"hba": [1]},
    },
    # --- multi-tool questions ---
    {
        "question": "Which has the higher TPSA: CCO or c1ccccc1O?",
        "expected_tools": ["calc_properties", "calc_properties"],
        "expected_values": {"tpsa": [20.23]},
    },
    {
        "question": "What is the TPSA of c1ccccc1O, and what is the pIC50 of its 2.5 nM IC50?",
        "expected_tools": ["calc_properties", "to_pic50"],
        "expected_values": {"tpsa": [20.23], "pic50": [8.60]},
    },
    {
        "question": "Can you give me the TPSA of c1ccccc1O and the convert its 2 batches of runs of IC50, first bacth is 2.5nM IC50 and second batch is 2.8nM to pIC50 ?",
        "expected_tools": ["calc_properties", "to_pic50", "to_pic50"],
        "expected_values": {"tpsa": [20.23], "pic50": [8.60, 8.55]},
    },
    # --- no tool needed ---
    {
        "question": "What is the capital of France?",
        "expected_tools": [],
        "expected_values": {},
    },
    {
        "question": "What is the capital of Germany?",
        "expected_tools": [],
        "expected_values": {},
    },
    {
        "question": "What is the molecular formula of aspirin?",
        "expected_tools": [],
        "expected_values": {},
    },
    # --- tricky inputs: the agent should ask or explain, not calculate ---
    {
        "question": "What is the TPSA of xyz1234?",
        "expected_tools": [],
        "expected_values": {},
    },
    {
        "question": "What is the pIc50 of 250?",
        "expected_tools": [],
        "expected_values": {},
    },
    {
        "question": "What is the pic50 of 0 nM?",
        "expected_tools": [],
        "expected_values": {},
    },
]
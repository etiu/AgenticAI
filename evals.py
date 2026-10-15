EVAL_CASES = [
    {
        "question": "What is the pIC50 of 250 nM?",
        "expected_tool": "to_pic50",
        "expected_value": 6.60,
    },
    {
        "question": "What is the TPSA of CCO?",
        "expected_tool": "calc_properties",
        "expected_value": 20.23,
    },
    {
        "question": "What is the capital of France?",
        "expected_tool": None,
        "expected_value": None,
    },
        {
        "question": "What is the Mw of CO?",
        "expected_tool": "calc_properties",
        "expected_value": 32.04,
    },
        {
            "question": "What is the Mw of CH4O?",
            "expected_tool": "calc_properties",
            "expected_value": None,
    },
        {
        "question": "What is the mol weight of CCO?",
        "expected_tool": "calc_properties",
        "expected_value": 46.07,
    },
        {
        "question": "How many HBD are there in CCO?",
        "expected_tool": "calc_properties",
        "expected_value": 1,
    },
        {
        "question": "What is the Hydrog bond acceptor count of CCO?",
        "expected_tool": "calc_properties",
        "expected_value": 1,
    },
        {
        "question": "What is the capital of Germany?",
        "expected_tool": None,
        "expected_value": None, 
    },
        {
        "question": "What is the molecular formula of aspirin?",
        "expected_tool": None,
        "expected_value": None,
    },
        {
        "question": "What is the pIC50 of 2.5 M?",
        "expected_tool": "to_pic50",
        "expected_value": -0.40,
    },
        {
        "question": "What is the pIC50 of 0.25 micromolar?",
        "expected_tool": "to_pic50",
        "expected_value": 6.60,
    },
        {
        "question": "What is the pIC50 of 250 pM?",
        "expected_tool": "to_pic50",
        "expected_value": 9.60,
    },
        {
        "question": "What is the TPSA of xyz1234?",
        "expected_tool": "calc_properties",
        "expected_value": None,
    },
        {
        "question": "What is the pIc50 of 250?",
        "expected_tool": None, 
        "expected_value": None,
        },
        {
        "question": "What is the pic50 of 0 nM?",
        "expected_tool": "to_pic50",
        "expected_value": None,
},
]
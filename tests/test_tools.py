from tools import calc_properties


def test_calc_properties_ethanol():
    props = calc_properties("CCO")
    assert props["mol_weight"] == 46.07
    assert props["tpsa"] == 20.23
    assert props["hbd"] == 1
    assert set(props) == {"smiles", "mol_weight", "clogp", "tpsa", "hbd", "hba"}

def test_calc_properties_invalid():
    bad = calc_properties("not_a_smiles")
    assert "error" in bad
    assert "error" in calc_properties("")


def test_to_pic50():
    assert "error" in to_pic50(None, "mM") 
assert "error" in to_pic50(0 , "nM")
assert "error" in to_pic50(250, "M")
assert "error" in to_pic50(-5, "nM")
assert round(to_pic50(250, "pM"), 2) == 9.60     # calculation, pM
assert round(to_pic50(250, "nM"), 2) == 6.60     # calculation, nM
assert round(to_pic50(0.25, "uM"), 2) == 6.60    # calculation, uM
assert round(to_pic50(0.25, "mM"), 2) == 3.60    # calculation, mM


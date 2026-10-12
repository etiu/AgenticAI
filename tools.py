from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen, rdMolDescriptors, Lipinski

def calc_properties(smi: str) -> dict:
    props = {}
    if smi == "":
        return {'error': "Empty SMILES string"}
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return {'error': f'Invalid SMILES: {smi!r}'}
    mw = round(Descriptors.MolWt(mol), 2)
    logp = round(Crippen.MolLogP(mol), 2)
    tpsa = round(rdMolDescriptors.CalcTPSA(mol), 2)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)
    props['smiles'] = smi
    props['mol_weight'] = mw
    props['clogp'] = logp
    props['tpsa'] = tpsa
    props['hbd'] = hbd
    props['hba'] = hba
    return props

props = calc_properties("CCO")
assert props["mol_weight"] == 46.07
assert props["tpsa"] == 20.23
assert props["hbd"] == 1
assert set(props) == {"smiles", "mol_weight", "clogp", "tpsa", "hbd", "hba"}

bad = calc_properties("not_a_smiles")
assert "error" in bad
assert "error" in calc_properties("")
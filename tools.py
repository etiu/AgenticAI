from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen, rdMolDescriptors, Lipinski
import math


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


UNIT_CONV = {'pM': 0.001, 'nM': 1, 'uM': 1000, 'mM': 1000000}

def to_pic50(value: float, units: str) -> float | dict:
    if units not in UNIT_CONV:
        return {"error": "unsupported units. try pM, uM, nM, or mM."}
    if not isinstance(value, (int, float)):
        return {"error": "invalid value. value must be a number"}
    if value <=0:
        return {"error": "invalid value. try a nonzero, positive number"}
    
    new_val = value*UNIT_CONV[units]
    val_pic50 = 9 - math.log10(new_val)
    return val_pic50
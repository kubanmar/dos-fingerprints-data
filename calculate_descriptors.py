# file: calculate_descriptors.py
# Calculate PTE and SG descriptors as defined in: 
# "Density-of-states similarity descriptor for unsupervised learning from materials data" 
# by Martin Kuban, Santiago Rigamonti, Markus Scheidgen, and Claudia Draxl, preprint: https://arxiv.org/abs/2201.02187 
# Requires a SQLite database file called 'c2db.db', as created by ASEs AtomsDatabase (https://wiki.fysik.dtu.dk/ase/ase/db/db.html), 
# which contains atomic structures for the materials that for which the descriptors should be calculated. 

from ase import Atoms
from ase.spacegroup import get_spacegroup
import numpy as np

PTE = {1: 1, 2: 2, 3: 1, 4: 2, 5: 13, 6: 14, 7: 15, 8: 16, 9: 17, 10: 18, 11: 1, 12: 2, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 1, 20: 2, 
    21: 3, 22: 4, 23: 5, 24: 6, 25: 7, 26: 8, 27: 9, 28: 10, 29: 11, 30: 12, 31: 13, 32: 14, 33: 15, 34: 16, 35: 17, 36: 18, 37: 1, 38: 2, 39: 3, 40: 4,
    41: 5, 42: 6, 43: 7, 44: 8, 45: 9, 46: 10, 47: 11, 48: 12, 49: 13, 50: 14, 51: 15, 52: 16, 53: 17, 54: 18, 55: 1, 56: 2, 57: 3, 72: 4, 73: 5, 74: 6, 
    75: 7, 76: 8, 77: 9, 78: 10, 79: 11, 80: 12, 81: 13, 82: 14, 83: 15, 84: 16, 85: 17, 86: 18, 87: 1, 88: 2, 89: 3, 104: 4, 105: 5, 106: 6, 107: 7, 
    108: 8, 109: 9, 110: 10, 111: 11, 112: 12, 113: 13, 114: 14, 115: 15, 116: 16, 117: 17, 118: 18}

def get_PTE_descriptor(atoms: Atoms) -> np.float64:
    """
    Calculate PTE descriptor value. 
    The PTE descriptor is the average of the column number of atomic species over all atoms in a unit cell.

    **Arguments:**
    
    atoms: ``ase.Atoms``
        `Atoms` object as provided by the Atomic Simulation Environement

    **Returns**

    pte_value: ``numpy.float64``
        Descriptor value.
    """
    return np.mean([PTE[atomic_number] for atomic_number in atoms.get_atomic_numbers()])

def get_SG_descriptor(atoms: Atoms) -> int:
    """
    Calculate the SG descriptor value.
    The SG descriptor is the space group number of a crystal lattice, ignoring atomic species.

    **Arguments:**
    
    atoms: ``ase.Atoms``
        `Atoms` object as provided by the Atomic Simulation Environement

    **Returns**

    sg_value: ``int``
        Descriptor value.
    """
    atoms.set_atomic_numbers([1 for _ in atoms.get_atomic_numbers()])
    return get_spacegroup(atoms, symprec=1e-1).no

def main():
    from ase.db import connect

    database = connect("c2db.db")
 
    print(f"Structure id\tPTE\tSG")
    for db_index in range(1, len(database) + 1):
        db_entry = database[db_index]
        atoms = db_entry.toatoms()
        print(f"{db_entry.uid}\t{get_PTE_descriptor(atoms)}\t{get_SG_descriptor(atoms)}")

if __name__ == "__main__":
    main()
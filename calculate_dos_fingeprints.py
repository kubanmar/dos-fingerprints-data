# file: calculate_dos_fingerprints.py
# Calculate electronic density-of-states fingerprints.
# Executing this script generates the json file `dos_fingerprint_data.json`, which contains the serialized fingerprint data. 

import nomad_dos_fingerprints
import json

def get_dos_fingerprint(energy: list, dos: list) -> nomad_dos_fingerprints.DOSFingerprint:
    """
    Get DOS fingerprint.

    **Arguments:**

    energy: ``list``
        List of DOS energies in units of [eV]

    dos: ``list``
        List of DOS values in units of [states/eV/area]
    """
    return nomad_dos_fingerprints.DOSFingerprint(stepsize = 0.001).calculate(energy, dos, grid_id='dg_cut:512:0:4:(-3, 3):1024', convert_data = None)

def main():
    with open("dos_data_and_fingerprints.json", "r") as data_file:
        data = json.load(data_file)

    dos_fingerprint_data = {}

    for key, values in data.items():
        energy = values["energy"]
        dos = values["dos"]
        fingerprint = get_dos_fingerprint(energy, dos).to_dict()
        dos_fingerprint_data[key] = fingerprint
    
    with open("dos_fingerprint_data.json", "w") as out_file:
        json.dump(dos_fingerprint_data, out_file)

if __name__ == "__main__":
    main()
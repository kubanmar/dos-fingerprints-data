# Descriptors and similarity matrix for article "Density-of-states similarity descriptor for unsupervised learning from materials data" by Martin Kuban, Santiago Rigamonti, Markus Scheidgen, and Claudia Draxl

This repository contains the data used in the publication "Density-of-states similarity descriptor for unsupervised learning from materials data" by Martin Kuban, Santiago Rigamonti, Markus Scheidgen, and Claudia Draxl, preprint: https://arxiv.org/abs/2201.02187.

## Description of files

* `dos_data_and_fingerprints.json`
    
    This `json` file contains the following data
    
    * Total electronic densities of states (TDOS) of materials in the C2DB [1-3]. Data IDs are correspond with the C2DB.
    * Periodic table of elements (PTE) descriptors
    * Space group (SG) descriptors

* `DOS_similarity_matrix.csv`

    * Similarity matrix. Data IDs correspond with the C2DB.
    * Rows and columns contain similarity values between materials
    * To load the data to a `Python` object, you can use, e.g., `pandas.read_csv()` 

Both files are compressed and need to be expanded first, e.g. using `unzip`.

* `calculate_descriptors.py` 

    Python script to calculate the PTE and SG desciptor values. See Notes below 

* `calculate_dos_fingerprints.py`
    
    Python script to compute DOS fingerprints. See Notes below
    
## Notes

### Creation of ASE Atoms database for running script `calculate_descriptors.py`

To run the script `calculate_descriptors.py`, an ASE database with atomic structure is required. The data required for this can be downloaded from the C2DB website [3]. To create this required `c2db.db` file, visit the C2DB website [3] and click on `Browse data`. In the following search interface, modify the search parameters to include all materials. For each of the found materials, click on the button `Download` below the crystal structure viewer. The atomic simulation environment (ASE) [4] can be used to transform the downloaded structure files to the database file: Import each file using the `ase.io` module and `write` it to a `ase.db.core.Database` object.

### How to obtain the DOS fingerprints

The DOS fingerprints can be obtained from file, by loading `dos_data_and_fingerprints.json` and using the `nomad_dos_fingerprint.DOSFingerprint.from_dict()` method. Alternatively, they can be generated using the script `calculate_dos_fingerprints.py`. The execution requires a Python package, which can be downloaded from [4]. 

## References

[1] "The Computational 2D Materials Database: High-Throughput Modeling and Discovery of Atomically Thin Crystals"
Sten Haastrup, Mikkel Strange, Mohnish Pandey, Thorsten Deilmann, Per S. Schmidt, Nicki F. Hinsche, Morten N. Gjerding, Daniele Torelli, Peter M. Larsen, Anders C. Riis-Jensen, Jakob Gath, Karsten W. Jacobsen, Jens Jørgen Mortensen, Thomas Olsen, Kristian S. Thygesen
2D Materials 5, 042002 (2018)

[2] "Recent Progress of the Computational 2D Materials Database (C2DB)"
M. N. Gjerding, A. Taghizadeh, A. Rasmussen, S. Ali, F. Bertoldo, T. Deilmann, U. P. Holguin, N. R. Knøsgaard, M. Kruse, A. H. Larsen, S. Manti, T. G. Pedersen, T. Skovhus, M. K. Svendsen, J. J. Mortensen, T. Olsen, K. S. Thygesen
2D Materials 8, 044002 (2021)

[3] https://cmr.fysik.dtu.dk/c2db/c2db.html

[4] https://github.com/kubanmar/dos-fingerprints
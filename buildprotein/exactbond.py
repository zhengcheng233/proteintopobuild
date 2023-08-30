#!/usr/bin/env python 
import parmed as pmd
import numpy as np
# Load the topology file
top = pmd.load_file('UR.prmtop')

# Print bond information
bonds = []
for bond in top.bonds:
    bonds.append([bond.atom1.idx, bond.atom2.idx])

coords = []; symbols = []; res = []
with open('UR.pdb','r') as fp:
    lines = fp.readlines()[1:]
    for line in lines:
        line = line.strip().split()
        if len(line) == 10:
            symbols.append(line[2][0])
            res.append(line[3])
            coords.append([float(line[5]),float(line[6]),float(line[7])])

np.savez('init.npz', coord = coords, symbol = symbols, bond = bonds, res=res)

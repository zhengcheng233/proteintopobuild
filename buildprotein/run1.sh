source leaprc.protein.ff14SB
UR = sequence{ACE ALA ALA ALA ALA NME}
savepdb UR UR.pdb
saveamberparm UR UR.prmtop UR.inpcrd

tleap -f ALA.sh

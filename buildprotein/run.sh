source leaprc.protein.ff14SB
source leaprc.water.tip3p 
UR = sequence{ACE ALA ALA ALA ALA NME}
solvatebox UR TIP3PBOX 8.0
savepdb UR UR.pdb
saveamberparm UR UR.prmtop UR.inpcrd

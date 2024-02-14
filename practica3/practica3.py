from congrucialMixto import GPCM

gpcm = GPCM(a=5,semilla=4,c=7,m=10)
for i in range(8):
    print(gpcm.generate())
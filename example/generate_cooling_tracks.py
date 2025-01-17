import numpy as np
from matplotlib import pyplot as plt
from WDPhotTools.atmosphere_model_reader import atm_reader

atm = atm_reader()

# Default passband is G3
G = atm.interp_atm()
BP = atm.interp_atm(dependent='G3_BP')
RP = atm.interp_atm(dependent='G3_RP')

logg = np.arange(7., 9.5, 0.5)
Mbol = np.arange(0., 20., 0.1)

plt.figure(1, figsize=(8, 8))
for i in logg:
    logg_i = np.ones_like(Mbol) * i
    plt.plot(BP(logg_i, Mbol) - RP(logg_i, Mbol),
             G(logg_i, Mbol),
             label=r"$\log(g) = {}$".format(i))

plt.ylim(20., 6.)
plt.grid()
plt.legend()
plt.xlabel('(BP - RP) / mag')
plt.ylabel('G / mag')
plt.title('DA Cooling tracks')
plt.tight_layout()
plt.savefig('DA_cooling_tracks.png')

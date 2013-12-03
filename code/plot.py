from pylab    import *
from scipy.io import loadmat

data = loadmat('../data/killerYeast.mat')

sod1 = data['S_OD_1'][0]
sod2 = data['S_OD_2'][0]

svh1 = data['S_vvh_1'][0]
svh2 = data['S_vvh_2'][0]

kvh1 = data['K_vvh_1'][0]
kvh2 = data['K_vvh_2'][0]

kod1 = data['K_OD_1'][0]
kod2 = data['K_OD_2'][0]


fig = figure(figsize=(10,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

axs  = [ax1, ax2]
ods  = [[sod1, sod2], [kod1, kod2]]
vhs  = [[svh1, svh2], [kvh1, kvh2]]
tits = [r'Sensitive', r'Killer']

for ax, tit, od, vh in zip(axs, tits, ods, vhs):
  ax.plot(vh[0], od[0], 'ko', label='Vessel 1')
  ax.plot(vh[1], od[1], 'ro', label='Vessel 2')
  ax.set_xlabel(r'$F$ [Volumes/Hr]')
  ax.set_ylabel(r'Optical Density $\bar{\rho}$')
  ax.set_title(tit)
  ax.grid()
  leg = ax.legend()
  leg.get_frame().set_alpha(0.5)
tight_layout()
savefig('../doc/images/data.png', dpi=300)
show()


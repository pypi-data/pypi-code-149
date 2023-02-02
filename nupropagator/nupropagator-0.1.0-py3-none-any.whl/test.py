from types import SimpleNamespace
opts = SimpleNamespace()
opts.neutrinoPrimary_energy_mode = 'random'
opts.neutrinoPrimary_direction_mode = 'random'
opts.neutrinoPrimary_target_mode = 'random'
opts.neutrinoPrimary_current_mode = 'random'
opts.neutrinoPrimary_pdgid = 14
opts.neutrinoPrimary_energy_GeV = 10**2 
opts.neutrinoPrimary_direction = [0,0,1]
opts.neutrinoPrimary_pdf_model = 'CT10nlo'
opts.neutrinoPrimary_target = 2212

import time as time
import nupropagator.nugen as  nugen
import numpy as np


N =1000
nu = nugen.NuGen()
print('start')
tt1 = np.zeros(N)
tt2 = np.zeros(N)
n1 = 0
n2 = 0
for i in range(N):
    print('EVENT ', i)
    tt1[i] = time.time()
    n1 = nu.get_event(opts)
    tt1[i] = time.time()-tt1[i]
    tt2[i] = time.time()
    #n2 = nu.get_event_fix_en(opts)
    tt2[i] = time.time()-tt2[i]

print('1',n1)
print('2',n2)
print('time1',tt1.sum())
print('time2',tt2.mean())

print('end')

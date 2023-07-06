import argparse
import os
import numpy as np
import pandas as pd
from nsd_access import NSDAccess
import scipy.io

def main():
    nsda = NSDAccess('../../nsd/')
    nsd_expdesign = scipy.io.loadmat('../../nsd/nsddata/experiments/nsd/nsd_expdesign.mat')

    # Note that most of nsd_expdesign indices are 1-base index!
    # This is why subtracting 1
    sharedix = nsd_expdesign['sharedix'] -1 
    print(sharedix.shape)
    exit()

    # Use for ave
    stims = np.load(f'../../mrifeat/subj01/subj01_stims_ave.npy')

    # Use for each
    # stims = np.load(f'../../mrifeat/subj01/subj01_stims.npy')
    # 27750 = 37 session * 750 scan


    print(type(stims))
    print(stims.shape)
    # print(stims[:3])

    exit()

    behs = pd.DataFrame()
    beh = nsda.read_behavior(subject='subj01', session_index=0)

    print(behs)
    print('fin')

    exit()
    '''
    for i in range(1,38):
        beh = nsda.read_behavior(subject=subject, 
                                session_index=i)
    '''
    if not os.path.exists(f'../../mrifeat/subj01_stims.npy'):
        np.save(f'{savedir}/{subject}_stims.npy',stims_all)
        np.save(f'{savedir}/{subject}_stims_ave.npy',stims_unique)

    stims_all = np.load('../../mrifeat/subj01/subj01_stims.npy')
    print(type(stims_all))
    # stims_unique = np.load('../../mrifeat/subj01/subj01_stims_ave.npy')

if __name__ == "__main__":
    main()

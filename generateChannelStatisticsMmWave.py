# sudo vim /etc/ld.so.conf
#    Add ./build/lib
# sudo ldconfig -v

import scipy.io as sio
import numpy as np
from subprocess import Popen, PIPE
import time
import datetime

def getSinr(ue_loc):
    process = Popen("./build/scratch/mmwave-sinr-singleUE -x=" + str(ue_loc) + " -RngRun=" + str(np.random.randint(1, 1000000)), shell=True, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    exit_code = process.wait()
    return float(err.split()[-1])

ue_num = 20
cell_range = 150
ue_loc_list = np.random.rand(ue_num) * cell_range + 1
ue_sinr_list = np.zeros(ue_num)
for idx in range(ue_num):
    ue_sinr_list[idx] = getSinr(ue_loc_list[idx])
sio.savemat('./sinr_trace/' + datetime.datetime.now().strftime("%Y%m%d-%H%M") + '.mat', {'ue_loc': ue_loc_list, 'sinr': ue_sinr_list})
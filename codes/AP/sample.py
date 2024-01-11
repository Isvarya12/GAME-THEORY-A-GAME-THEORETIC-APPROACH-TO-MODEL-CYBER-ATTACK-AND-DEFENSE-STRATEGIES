#calculate and display payoff matrix
import pandas as pd
import numpy as np
from test import *
data = pd.read_csv('finaldataset.csv')
for i in range(data.shape[0]):
    i=1
    gain=float(data['g'][i])
    cm1=float(data['cm1'][i])
    cm2=float(data['cm2'][i])
    ci1=float(data['ci1'][i])
    ci2=float(data['ci2'][i])
    loss=float(data['l'][i])
    alpha=float(data['a'][i])
    beta=float(data['b'][i])

    M = pd.DataFrame(index=['No Attack', 'Low Attack', 'High Attack'], columns=['No defense', 'Low Defense', 'High Defense'])
    M.at['No Attack','No defense']=[0,0]
    M.at['No Attack', 'Low Defense'] = [0,-ci1]
    M.at['No Attack', 'High Defense'] = [0,ci2]

    M.at['Low Attack', 'No defense'] = [-cm1+gain , -loss]
    M.at['Low Attack', 'Low Defense'] = [-cm1+(1-alpha)*gain , -ci1-(1-alpha)*loss]
    M.at['Low Attack', 'High Defense'] = [-cm1+(1-beta)*gain, -ci2-(1-beta)*loss]

    M.at['High Attack', 'No defense'] = [-cm2+gain, -loss]
    M.at['High Attack', 'Low Defense'] = [-cm2+(1-alpha)*gain, -ci1-(1-alpha)*loss]
    M.at['High Attack', 'High Defense'] = [-cm2+(1-beta)*gain, -ci1-(1-beta)*loss]

    print(M)



    arr=np.array([
        [(0,0),(0,-ci1),(0,ci2)],
    [(-cm1+gain , -loss),(-cm1+(1-alpha)*gain , -ci1-(1-alpha)*loss),(-cm1+(1-beta)*gain, -ci2-(1-beta)*loss)]
    ,[(-cm2+gain, -loss),(-cm2+(1-alpha)*gain, -ci1-(1-alpha)*loss),(-cm2+(1-beta)*gain, -ci1-(1-beta)*loss)]])
    analyse(arr)
    # print(M)
    
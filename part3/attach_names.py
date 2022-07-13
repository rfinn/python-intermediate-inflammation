#!/usr/bin/env python

import numpy as np

def attach_names(data,names):
    assert len(data) == len(names)
    patients = []
    for i,n in enumerate(names):
        patients.append({'name':n,
                         'data':data[i].tolist()})

    return patients

data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

output = attach_names(data, ['Alice', 'Bob'])
print(output)


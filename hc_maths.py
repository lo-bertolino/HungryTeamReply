#!/usr/bin/env python3

import sys
import math
import logging
import eulogy
import argparse
import random
import selfishgenex as sgx

assert sys.version_info >= (3, 4)



stuff = None
#fitness function
def mathsfunction(vector):
    global stuff
    if stuff is None:
        stuff = [(random.randint(1,10),random.randint(-100,100)) for i in range(len(vector))]
        maxi=0
        for i in range(len(vector)):
            maxi = i if stuff[i][0]>stuff[maxi][0] else maxi
        stuff[maxi] = (stuff[maxi][0]+1,-abs(stuff[maxi][1])) if stuff[maxi][0]%2==1 else (stuff[maxi][0],-abs(stuff[maxi][1]))
        print(stuff)
    ans = 0
    for i,comp in enumerate(vector):
        ans += comp**stuff[i][0]*stuff[i][1]
    return ans

DIM = 1
#stepnumber=10000
def main():
    ind=[random.randint(1,10) for i in range(DIM)]#genes
    fitness = mathsfunction(ind)
    print(mathsfunction(ind),ind)
    last=list()
    while last!=ind:
        epsilon = 1#problem specific delta
        steps = []
        last=ind
        for j in range(DIM):
            steps.append(ind[:j]+[ind[j]+epsilon]+ind[j+1:])
            steps.append(ind[:j]+[ind[j]-epsilon]+ind[j+1:])
        for j in steps:
            ind = j if mathsfunction(j)>mathsfunction(ind) else ind 
        print(mathsfunction(ind),ind)
    print(mathsfunction(ind),ind)
if __name__ == "__main__":
    main()

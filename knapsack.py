#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
#              #                                                             #
#   #####      # The Extended Selfish Gene optimization library (SGX)        #
#  ######      # by Giovanni Squillero <giovanni.squillero@polito.it>        #
#  ###   \     #                                                             #
#   ##G  c\    # Yet another population-less evolutionary algorithm loosely  #
#   #     _\   # inspired by a cool interpretation of the Darwinian theory.  #
#   |  _/      # Project page: <https://github.com/squillero/sgx>            #
#              #                                                             #
##############################################################################
# Copyright © 2018 Giovanni Squillero. All rights reserved.                  #
# The SGX library is licensed under the GNU Lesser General Public License.   #
# This example is licensed under the Free Public License (aka. "0BSD").      #
##############################################################################

import sys
import math
import logging
import eulogy
import argparse
import random
import selfishgenex as sgx

assert sys.version_info >= (3, 4)

DIM = 10
THRESHOLD = DIM / 4.

def fitness(ind):
    tot_reward = tot_constraint = 0.
    for g in range(DIM):
        if ind[g]:
            tot_reward += reward[g]
            tot_constraint += constraint[g]
    if tot_constraint < THRESHOLD:
        fit = (tot_reward,)
    else:
        fit = (0,)

    return sgx.FitnessLexicographic(fit)


# use list of list to handle n-dim or multiple knapsack
reward = list()
constraint = list()

for i in range(DIM):
    reward.append(random.random())
    constraint.append(random.random())
print("reward",reward)
print("constraint",constraint)

ind = [1 for _ in range(DIM)]
print(ind, ": ", fitness(ind))
for _ in range(10):
    ind = [random.choice([0, 1]) for _ in range(DIM)]
    print(ind, ": ", fitness(ind))

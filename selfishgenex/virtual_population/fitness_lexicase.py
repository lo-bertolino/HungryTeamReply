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
##############################################################################

import sys
import random
import logging
from .fitness import Fitness


class FitnessLexicase(Fitness):
    """A fitness implementing "Lexicase Selection", a technique supposedly able
    to handle “uncompromising" multi-objective problems, i.e., where solutions
    must perform optimally on each of many test cases. See "Solving Uncompromising
    Problems With Lexicase Selection" by T. Helmuth, L. Spector, and J. Matheson
    (DOI: 10.1109/TEVC.2014.2362729)"""

    def __gt__(self, other):
        order = list(range(len(self)))
        random.shuffle(order)
        return tuple([self[i] for i in order]) > tuple([other[i] for i in order])

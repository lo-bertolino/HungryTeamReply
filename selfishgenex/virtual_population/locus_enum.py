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
##############################################################################

import math
import logging
import numpy as np
from .locus_base import LocusBase


def f(x, a):
    return 1. / (1. + math.exp(-a * x))

def inv_f(p, a):
    return math.log(p / (1 - p)) / a


class LocusEnum(LocusBase):
    """The 'traditional' SG locus: a set of enumerable alternatives"""

    def __init__(self, alleles, alpha=math.sqrt(7)/200., init_probs=None):
        assert hasattr(alleles, '__iter__'), \
            "ERROR:: Alleles must be iterable (found: {})".format(type(alleles))

        super().__init__()
        if init_probs is None:
            init_probs = dict()
        self._canonic_order = list(alleles)
        self.alleles = dict()
        self.alpha = alpha
        if not init_probs:
            for a in alleles:
                self.alleles[a] = 1. / len(alleles)
        else:
            p = 1.
            for a in init_probs:
                assert a in alleles, "ERROR:: Invalid allele: '" + str(a) + "'"
                assert init_probs[a] >= 0. and init_probs[a] <= 1., "ERROR:: Invalid initial probability: " + str(init_probs)
                self.alleles[a] = init_probs[a]
                p -= init_probs[a]
            assert p >= 0. and p <= 1., "ERROR:: Invalid initial probability: " + str(init_probs)
            p /= len(alleles) - len(self.alleles)
            for a in alleles:
                if a not in self.alleles:
                    self.alleles[a] = p
            assert self._sum() <= 1, "ERROR:: Invalid initial probability: " + str(init_probs)
        assert self._sum()

    def __str__(self):
        return self.signature() + \
            "{[" + ", ".join(["{}:{:0.4g}".format(repr(_), self.alleles[_]) \
                for _ in self._canonic_order]) + \
            "], α={:.4g}".format(self.alpha) + "}"

    def signature(self):
        return "λ{}".format(len(self.alleles))

    def _sum(self):
        s = sum(self.alleles.values())
        assert abs(1. - s) < 1e-10, "PANIC:: Inconsistent locus: 1-Σp={:g} in ".format(1.-s) + str(self)
        return s

    def update(self, winner, loser):
        assert winner in self.alleles, "ERROR:: Invalid allele: '" + str(winner) + "' -- expected in " + str(sorted(list(self.alleles.keys())))
        assert loser in self.alleles, "ERROR:: Invalid allele: '" + str(loser) + "' -- expected in " + str(sorted(list(self.alleles.keys())))
        # 1e-300 looks like a reasonably small number not to log(0.) ... see: sys.float_info
        x_winner = inv_f(1e-300 + self.alleles[winner], self.alpha)
        delta = min(self.alleles[loser], f(x_winner+1, self.alpha) - f(x_winner, self.alpha))
        self.alleles[winner] += delta
        self.alleles[loser] -= delta
        # logging.debug("Allele: %s", self.alleles)
        assert self._sum()

    def get(self, method='sample'):
        if method == 'sample':
            return np.random.choice(list(self.alleles.keys()), p=list(self.alleles.values()))
        elif method == 'mode':
            return max(self.alleles, key=self.alleles.get)
        elif method == 'random':
            return np.random.choice(list(self.alleles.keys()))
        else:
            assert method in ['sample', 'mode', 'random'], "ERROR: Unknown method '" + str(method) + "'"

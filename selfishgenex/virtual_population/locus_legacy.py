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

import logging
from .locus_enum import LocusEnum


class LocusEnum_Legacy(LocusEnum):
    """The 'traditional' SG locus: a set of enumerable alternatives"""

    def __init__(self, alleles, alpha=1e-3, **kwargs):
        super().__init__(alleles, alpha=alpha, **kwargs)

    def signature(self):
        return "λ{}/o".format(len(self.alleles))

    def update(self, winner, loser):
        assert winner in self.alleles, "ERROR:: Invalid allele: '" + str(winner) + "' -- expected in " + str(sorted(list(self.alleles.keys())))
        assert loser in self.alleles, "ERROR:: Invalid allele: '" + str(loser) + "' -- expected in " + str(sorted(list(self.alleles.keys())))
        delta = min(self.alpha, self.alleles[loser], 1. - self.alleles[winner])
        self.alleles[winner] += delta
        self.alleles[loser] -= delta
        assert self._sum()

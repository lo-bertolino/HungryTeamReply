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
import random
from ..utilities import describe_list


class AlleleDistribution():
    def __init__(self, loci):
        self._locus = tuple(loci)

    def __repr__(self):
        return '%s:%s' % (self.__class__, self.__dict__)

    def __str__(self):
        return "[" + describe_list([str(_) for _ in self._locus]) + "]"

    def __getitem__(self, locus_index):
        assert isinstance(locus_index, int), "Locus index must be integer (found '" + str(type(locus_index)) + "')"
        return self._locus[locus_index]

    def __len__(self):
        return len(self._locus)

    def get(self, mutation_probability=0.):
        individual = list()
        if not hasattr(mutation_probability, '__iter__'):
            mutation_probability = [mutation_probability] * len(self._locus)
        assert len(mutation_probability) == len(self._locus), "ERROR:: Wrong probability array: " + str(mutation_probability)
        #m = 0
        for g, p in zip(self._locus, mutation_probability):
            if p is not None:
                assert p >= 0. and p <= 1., "PANIC:: Wrong probability: p={}".format(p)
                if random.random() < p:
                    individual.append(g.get(method='random'))
                    #m += 1
                else:
                    individual.append(g.get(method='sample'))
            else:
                individual.append(g.get(method='mode'))
        #if m > 0:
        #    logging.warning("%g -> %d", p, m)
        return individual

    def update(self, winner, loser):
        for i in range(len(self._locus)):
            self._locus[i].update(winner=winner.genome[i], loser=loser.genome[i])

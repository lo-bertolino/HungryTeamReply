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

from ..utilities import describe_list, compact_list


class Individual:
    def __init__(self, genome, fitness, birth=0):
        assert genome is None or hasattr(genome, '__iter__'), "ERROR:: Genome must be iterable (found: {})".format(type(genome))
        assert (not genome and not fitness) or (genome and fitness), \
            "ERROR:: Illegal individual: genome={}, fitness={}".format(genome, fitness)
        self._genome = tuple(genome)
        self._fitness = fitness
        self._birth = birth

    def __str__(self):
        sep = ""
        dl = compact_list(self._genome)
        for g in dl:
            if len(str(g)) > 1:
                sep = ", "
        return sep.join([str(_) for _ in dl])

    def __repr__(self):
        return "I{[" + self.__str__() + "], f=" + str(self._fitness) + \
               ", ★:" + str(self._birth) + \
               "}"

    def __bool__(self):
        return self._genome is not None

    def __hash__(self):
        return hash(self._genome)

    def __eq__(self, other):
        assert isinstance(other.genome, tuple), str(type(other.genome)) + " " + repr(other.genome)
        return self._genome == other.genome

    @property
    def genome(self):
        return self._genome

    @property
    def fitness(self):
        return self._fitness

    @property
    def birth(self):
        return self._birth

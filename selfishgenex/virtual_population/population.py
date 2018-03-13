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

from .individual import Individual


class VirtualPopulation:
    def __init__(self, allele_distribution, fitness_function, mutation_probability=None):
        self.allele_distribution = allele_distribution
        self.fitness_function = fitness_function
        if mutation_probability is not None:
            self.mutation_probability = mutation_probability
        else:
            self.mutation_probability = 1. / len(allele_distribution)

    def extract_individual(self, generation=0):
        genome = self.allele_distribution.get(self.mutation_probability)
        fitness = self.fitness_function(genome)
        return Individual(genome, fitness, generation)

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


def pareto(individuals):
    individuals = set(individuals)
    pareto_set = set()
    for i in set(individuals):
        dominated = any([x.fitness.dominate(i.fitness) for x in individuals])
        if not dominated:
            pareto_set.add(i)

    #logging.info("ORIG: %s", individuals)
    #logging.info("NEW : %s", pareto_set)
    return pareto_set


def fit_dominate(fitness, pool):
    return all([fitness > i for i in pool])


def fit_dominated(fitness, pool):
    return any([fitness <= i for i in pool])

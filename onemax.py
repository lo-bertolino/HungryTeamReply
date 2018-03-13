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
import selfishgenex as sgx

assert sys.version_info >= (3, 4)


def one_max(ind):
    """ The simplest test problem in the west """
    return sgx.FitnessLexicographic(sum(ind) / len(ind))


def main(zeta):
    """ Just main(), what else? """

    g = sgx.AlleleDistribution(zeta)
    logging.debug("New Allele Distribution: %s", g)
    filename = "1max_{}.dat".format(0)
    opt = sgx.VanillaOptimizer(g, one_max,
                               max_fitness=sgx.FitnessLexicographic(1.),
                               #aggregate_fitness=lambda i: one_max(i)[0],
                               #max_aggregate_fitness=1.,
                               archive_max_size=None,
                               mutation_probability=None, fitness_log=filename)
    # opt = sgx.VanillaOptimizer(g, one_max, max_generations=250, max_fitness=1.)

    opt.evolve()
    logging.info("Solution: %s", opt.archive)


if __name__ == "__main__":
    eulogy.init_logging(console_log_level=eulogy.INFO)
    logging.log(eulogy.WARNING_RAW, r'   __________  __ ')
    logging.log(eulogy.WARNING_RAW, r'  / __/ ___/ |/_/  Extended Selfish Gene sgx_0.1')
    logging.log(eulogy.WARNING_RAW, r' _\ \/ (_ />  <    Copyright (c) 2018 Giovanni Squillero')
    logging.log(eulogy.WARNING_RAW, r'/___/\___/_/|_|    ')
    logging.log(eulogy.WARNING_RAW, r'                   ')

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", dest="verbose", default=0, help="increase log verbosity")
    parser.add_argument("-d", "--debug", action="store_const", dest="verbose", const=2, help="log debug messages (same as -vv)")
    parser.add_argument("-o", "--old-update", action="store_const", dest="old_update_algorithm", const=True, help="Use old SG update algorithm")
    args = parser.parse_args()

    if args.verbose == 0:
        eulogy.init_logging(console_log_level=eulogy.WARNING)
    elif args.verbose == 1:
        eulogy.init_logging(console_log_level=eulogy.INFO)
    elif args.verbose == 2:
        eulogy.init_logging(enable_debug_log=True)

    z = list()
    NUM = 1000
    if not args.old_update_algorithm:
        logging.info("Using new sigmoid update")
        for _ in range(NUM):
            z.append(sgx.LocusEnum([0, 1]))
    else:
        logging.info("Using old linear update")
        for _ in range(NUM):
            z.append(sgx.LocusEnum_Legacy([0, 1]))

    main(z)

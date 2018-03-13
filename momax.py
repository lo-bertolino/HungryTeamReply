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
import random
import logging
import eulogy
import signal
import time
import selfishgenex as sgx

SIZE = 10
PATTERNS = 3
MOMAX_TARGETS = list()


class handler_helper:
    last_sigint = 0


def momax(ind):
    global_fitness = list()
    for target in MOMAX_TARGETS:
        fitness = 0
        valid_bits = 0
        for i, t in zip(ind, target):
            if t != '-':
                valid_bits += 1
            if i == t:
                fitness += 1
        global_fitness.append(fitness / valid_bits)
    return sgx.FitnessLexicase(global_fitness)


def momax_aggregate(ind):
    aggregate_fitness = 0.
    for target in MOMAX_TARGETS:
        fitness = 0
        valid_bits = 0
        for i, t in zip(ind, target):
            if t != '-':
                valid_bits += 1
            if i == t:
                fitness += 1
        aggregate_fitness += fitness / valid_bits
    return aggregate_fitness / PATTERNS


def main():
    """ Just main(), what else? """

    for _ in range(PATTERNS):
        p = ""
        for _ in range(SIZE):
            p = p + random.choice("-01")
        MOMAX_TARGETS.append(p)

    logging.info("TARGET PATTERNS")
    for p in MOMAX_TARGETS:
        logging.info(p)

    z = list()
    for _ in range(SIZE):
        z.append(sgx.LocusEnum("01"))
    g = sgx.AlleleDistribution(z)
    logging.info("New Allele Distribution: %s", g)
    opt = sgx.VanillaOptimizer(g, momax,
                               aggregate_fitness=momax_aggregate, max_aggregate_fitness=1.,
                               archive_max_size=10,
                               verbose=True,
                               max_generations=10000)
    # opt = sgx.VanillaOptimizer(g, momax, max_generations=250, max_fitness=1.)

    h = handler_helper
    h.last_sigint = 0.

    def handler(signum, stackframe):
        now = time.time()
        if now - h.last_sigint < 2:
            signal.default_int_handler(signum, stackframe)
        logging.info("Caught SIGINT -- hit twice to raise KeyboardInterrupt")
        opt.request_dump()
        h.last_sigint = now

    signal.signal(signal.SIGINT, handler)

    opt.evolve()
    logging.info("Solution: %s", repr(opt.archive))
    logging.info("")
    logging.info(opt.archive)
    for p in MOMAX_TARGETS:
        logging.info(p)
    logging.info("")
    sys.exit()


if __name__ == "__main__":
    eulogy.init_logging(console_log_level=eulogy.INFO)
    logging.log(eulogy.WARNING_RAW, r'   __________  __ ')
    logging.log(eulogy.WARNING_RAW, r'  / __/ ___/ |/_/  Extended Selfish Gene sgx_0.1')
    logging.log(eulogy.WARNING_RAW, r' _\ \/ (_ />  <    Copyright (c) 2018 Giovanni Squillero')
    logging.log(eulogy.WARNING_RAW, r'/___/\___/_/|_|    ')
    logging.log(eulogy.WARNING_RAW, r'                   ')
    main()

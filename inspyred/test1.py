#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################################
#             #                                                            #
#   #####     # (!) Giovanni Squillero <giovanni.squillero@polito.it>      #
#  ######     #                                                            #
#  ###   \    # Copying and distributing this file, either with or without #
#   ##G  c\   # modification, is permitted in any medium without royalty,  #
#   #     _\  # provided that this 10-line comment is preserved.           #
#   |  _/     # THIS FILE IS OFFERED AS-IS, WITHOUT ANY WARRANTY.          #
#             #                                                            #
############################################################################

import logging
import sys
import random
import time
import inspyred

assert sys.version_info >= (3, 4)


class myfit(tuple):
    def __format__(self, fmt):
        return str(self[0])


def generate_binary(random, args):
    bits = args.get('num_bits', 8)
    return [random.choice([0, 1]) for i in range(bits)]


@inspyred.ec.evaluators.evaluator
def evaluate_binary(candidate, args):
    fit = int("".join([str(c) for c in candidate]), 2)
    logging.info("%s", candidate)
    logging.info("--> %s", fit)
    return myfit((fit, 0, 42))


logging.getLogger().setLevel(level=logging.DEBUG)

rand = random.Random()
rand.seed(int(time.time()))
ga = inspyred.ec.GA(rand)
ga.observer = inspyred.ec.observers.stats_observer
ga.terminator = inspyred.ec.terminators.evaluation_termination
final_pop = ga.evolve(evaluator=evaluate_binary,
                      generator=generate_binary,
                      max_evaluations=1000,
                      num_elites=1,
                      pop_size=100,
                      num_bits=10)
final_pop.sort(reverse=False)
for ind in final_pop:
    print(str(ind))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################
#        __ __                          ______                   #
#       / // /_ _____  ___ _______ __  /_  __/__ ___ ___ _       #
#      / _  / // / _ \/ _ `/ __/ // /   / / / -_) _ `/  ' \      #
#     /_//_/\_,_/_//_/\_, /_/  \_, /   /_/  \__/\_,_/_/_/_/      #
#                    /___/    /___/                              #
#                                                                #
##################################################################

import sys
import logging
import argparse
import selfishgenex as sgx

assert sys.version_info >= (3, 4)

LOG_NAME = "1max_{}.dat".format(0)


def main():
    loci = list()
    genome_len = 1000  # h*w
    for _ in range(genome_len):
        if args.init_prob is not None:
            init_prob_dict = {0: args.init_prob}
        else:
            init_prob_dict = None

        loci.append(sgx.LocusEnum([0, 1], init_probs=init_prob_dict))

    genome = sgx.AlleleDistribution(loci)
    logging.debug("New Allele Distribution: %s", genome)

    opt = sgx.VanillaOptimizer(genome, fitness_function,
                               max_fitness=sgx.FitnessLexicographic(1.),
                               archive_max_size=5, fitness_log=LOG_NAME,
                               mutation_probability=args.mut_prob)
    # per aggiungere condizioni di terminazione
    # opt._stopping_conditions.append(lambda: _steady_state_function(opt, args.steady_state))

    opt.evolve()  # esecuzione dell'evolutivo

    if len(opt.archive) is 0:
        logging.error("Archivio vuoto! Non c'è soluzione!")
    else:
        result = opt.archive.pop()
        logging.info("Solution: %s", result)


def fitness_function(genome):
    # OBIETTIVO -> massimizzare il numero di celle a 1
    # return tuple(sum(genome)/len(genome))
    return sgx.FitnessLexicographic(sum(genome) / len(genome))


def _steady_state_function(optimizer, max_gen_without_improvement):
    to_stop = False

    for i in optimizer.archive:
        if (optimizer.generation - i.birth) > max_gen_without_improvement:
            to_stop = True
            logging.warning("Steady state reached! - Generation %d", optimizer.generation)
            break

    return to_stop


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", datefmt="%H:%M:%S")
    logging.getLogger().handlers[0].setFormatter(logging.Formatter('%(message)s'))
    logging.warning("##################################################################")
    logging.warning("#        __ __                          ______                   #")
    logging.warning("#       / // /_ _____  ___ _______ __  /_  __/__ ___ ___ _       #")
    logging.warning("#      / _  / // / _ \/ _ `/ __/ // /   / / / -_) _ `/  ' \      #")
    logging.warning("#     /_//_/\_,_/_//_/\_, /_/  \_, /   /_/  \__/\_,_/_/_/_/      #")
    logging.warning("#                    /___/    /___/                              #")
    logging.warning("#                                                                #")
    logging.warning("##################################################################")

    parser = argparse.ArgumentParser(description='Hungry Team Optimization process')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug option')
    parser.add_argument('-ip', '--init-prob', dest='init_prob', default=None, type=float,
                        help='Initial probability of having 0 values in the chromosome - rate [0.0-1.0]')
    parser.add_argument('-mp', '--mut-prob', dest='mut_prob', default=None, type=float,
                        help='Mutation probability rate [0.0-1.0]')
    parser.add_argument('-ss', '--steady-state', dest='steady_state', default=4000, type=int,
                        help="The maximum number of generation explored without improvements")
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(level=logging.DEBUG)
    else:
        logging.getLogger().setLevel(level=logging.INFO)

    logging.getLogger().handlers[0].setFormatter(logging.Formatter(
        "%(asctime)s.%(msecs)04d %(levelname)s: %(message)s", datefmt="%H:%M:%S"))

    main()
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
        loci.append(sgx.LocusEnum([0, 1]))

    genome = sgx.AlleleDistribution(loci)
    logging.debug("New Allele Distribution: %s", genome)

    opt = sgx.VanillaOptimizer(genome, fitness_function,
                               max_fitness=sgx.FitnessLexicographic(1.),
                               archive_max_size=5, fitness_log=LOG_NAME,
                               mutation_probability=None)
    opt.evolve()
    if len(opt.archive) is 0:
        logging.error("Archivio vuoto! Non c'è soluzione!")
    else:
        result = opt.archive.pop()
        logging.info("Solution: %s", result)


def fitness_function(genome):
    # OBIETTIVO -> massimizzare il numero di celle a 1
    # return tuple(sum(genome)/len(genome))
    return sgx.FitnessLexicographic(sum(genome) / len(genome))


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
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(level=logging.DEBUG)
    else:
        logging.getLogger().setLevel(level=logging.INFO)

    logging.getLogger().handlers[0].setFormatter(logging.Formatter(
        "%(asctime)s.%(msecs)04d %(levelname)s: %(message)s", datefmt="%H:%M:%S"))

    main()

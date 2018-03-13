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
from ..virtual_population.population import VirtualPopulation
from ..virtual_population.fitness import Fitness
from ..pareto import pareto
from ..pareto import fit_dominated
from ..utilities import plural


class VanillaOptimizer:
    """An optimizer implementing the simple, basic algorithm described in
    "The selfish gene algorithm: a new evolutionary optimization strategy"
    by F. Corno, M. Sonza Reorda, G. Squillero (DOI: 10.1145/330560.330838)"""

    def __init__(self, genome, fitness,
                 aggregate_fitness=None, max_aggregate_fitness=None,
                 max_fitness=Fitness(None), max_generations=None,
                 mutation_probability=None,
                 archive_max_size=None,
                 verbose=True,
                 fitness_log=None):

        assert archive_max_size is None or archive_max_size > 0
        self._population = VirtualPopulation(genome, fitness, mutation_probability=mutation_probability)
        self._stopping_conditions = list()
        self._generation = 0
        self._archive = set()
        self._before_extraction_hook = list()
        self._after_extraction_hook = list()
        self._initial_setup = list()
        self._final_wrapup = list()
        self._aggregate_fitness = aggregate_fitness
        self._max_aggregate_fitness = max_aggregate_fitness
        self._verbose = verbose
        self._fitness_log = fitness_log
        self._archive_max_size = archive_max_size
        self._dump_requested = False

        if aggregate_fitness:
            self._key_sort_function = lambda i: (aggregate_fitness(i.genome), i.birth)
        else:
            self._key_sort_function = lambda i: (i.birth,)

        if max_generations:
            self._stopping_conditions.append(lambda: self.generation >= max_generations)
        if max_fitness:
            self._stopping_conditions.append(lambda: fit_dominated(max_fitness, [i.fitness for i in self.archive]))
        if max_aggregate_fitness:
            self._stopping_conditions.append(lambda: any([aggregate_fitness(i.genome) > max_aggregate_fitness for i in self.archive]))

        # Handle a file-based fitness log
        if fitness_log:
            def fitness_log_open():
                self._fitness_log = open(fitness_log, "w")

            def fitness_log_dump(individuals):
                for i in individuals:
                    self._fitness_log.write(str(i.fitness) + "\n")

            self._initial_setup.append(fitness_log_open)
            self._after_extraction_hook.append(fitness_log_dump)
            self._final_wrapup.append(lambda: self._fitness_log.close)

    @property
    def generation(self):
        return self._generation

    @property
    def archive(self):
        return self._archive

    def request_dump(self):
        self._dump_requested = True

    def evolve(self):
        for f in self._initial_setup:
            f()
        while not any([_() for _ in self._stopping_conditions]):
            for f in self._before_extraction_hook:
                f(self._generation)
            self._generation += 1
            i1 = self._population.extract_individual(self._generation)
            i2 = self._population.extract_individual(self._generation)
            for f in self._after_extraction_hook:
                f([i1, i2])
            if i1.fitness == i2.fitness:
                # a tie, let's proceed
                continue

            if i1.fitness > i2.fitness:
                winner, loser = i1, i2
            else:
                winner, loser = i2, i1

            self._population.allele_distribution.update(winner, loser)
            # Note: the set operation guarantees that individual whose genome
            # is already in the archive are not considered for inclusion
            new_archive = pareto(self._archive | {i1, i2})
            assert new_archive, "{} {} {}".format(self._archive, {i1, i2}, new_archive)

            if self._archive_max_size:
                t = sorted(new_archive,
                           key=self._key_sort_function,
                           reverse=True)
                new_archive = set(t[:self._archive_max_size])

            status = list()
            if (self._archive != new_archive and self._verbose) or self._dump_requested:
                self._dump_requested = False
                logging.debug([i.fitness for i in new_archive])

                if self._aggregate_fitness:
                    val = max([self._aggregate_fitness(i.genome) for i in new_archive])
                    if self._max_aggregate_fitness:
                        status.append("Σ={:.2f}%".format(100.*val/self._max_aggregate_fitness))
                    else:
                        status.append("Σ={}".format(val))

                status.append("{} {} in archive".format(len(new_archive), plural("individual", len(new_archive))))

                logging.info("Generation %d: %s", self._generation, ", ".join(status))
                for n, i in enumerate(new_archive):
                    if self._aggregate_fitness:
                        val = self._aggregate_fitness(i.genome)
                        if self._max_aggregate_fitness:
                            aggregate_fitness_desc = " Σ={:.2f}%".format(100.*val/self._max_aggregate_fitness)
                        else:
                            aggregate_fitness_desc = " Σ={}".format(val)
                    else:
                        aggregate_fitness_desc = ""
                    logging.info("i%d:%s %s [%s]", n, aggregate_fitness_desc, i.fitness, i)

            self._archive = new_archive

        for f in self._final_wrapup:
            f()

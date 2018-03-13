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


class Fitness(tuple):
    """Base class for handling and comparing Fitness values (i.e., implementing
    different selection schemes). Derived classes are requested to implement
    __eq__ and __lt__"""

    def __new__(cls, fit):
        # Generic NEW that smoothly handles lists, tuples, and scalars
        if hasattr(fit, '__iter__'):
            return tuple.__new__(cls, fit)
        return tuple.__new__(cls, (fit,))

    # Standard methods
    def __bool__(self):
        """True iff all objectives are not None"""
        return all(v is not None for v in self)

    def __str__(self):
        return str(tuple(self))

    # Required
    def __gt__(self, other):
        """ Is self better than other? Override it to implement different selection schemes """
        raise NotImplementedError

    # Default
    def __eq__(self, other):
        """ True iff identical """
        return tuple(self) == tuple(other)

    def dominate(self, other):
        """ True iff self strictly dominates other """
        return all([s >= o for s, o in zip(self, other)]) and \
            any([s > o for s, o in zip(self, other)])

    # Methods that can be built upon __gt__ and __eq__
    def __ne__(self, other):
        # self != other
        return not self.__eq__(other)

    def __lt__(self, other):
        # self < other
        return not self.__gt__(other) and not self.__eq__(other)

    def __le__(self, other):
        # self <= other
        return not self.__gt__(other)

    def __ge__(self, other):
        # self >= other
        return self.__gt__(other) or self.__eq__(other)

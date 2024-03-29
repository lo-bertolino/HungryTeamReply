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

from .fitness import Fitness


class FitnessLexicographic(Fitness):
    """Tuples able to smoothly handle Nones, single- and multi-value fitnesses"""

    def __gt__(self, other):
        # Standard lexicographic
        if not self:
            return False
        elif not other:
            return True
        return tuple(self) > tuple(other)

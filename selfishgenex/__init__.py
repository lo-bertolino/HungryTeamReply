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

"""The Extended Selfish Gene optimization library (SGX)

Yet another population-less evolutionary algorithm loosely inspired
by a cool interpretation of the Darwinian theory.

Fore more information see <https://github.com/squillero/sgx>

Copyright © 2018 Giovanni Squillero. All rights reserved.
Licensed under the GNU Lesser General Public License (LGPL).
"""

import sys
import warnings
import logging

from .virtual_population import *
from .algorithms import *

#from .population import VirtualPopulation
#from .genemaps import Locus, Enum, Binary
#from .compare import compare_dictionary, compare_lexicase, compare_chromatic
#from .optimizer_vanilla import Vanilla

if sys.flags.optimize == 0:
    warnings.warn("All debug checks are active, performances may be impaired.", RuntimeWarning)

if sys.version_info < (3, 4):
    warnings.warn("The code has only been tested with Python v3.4+", Warning)

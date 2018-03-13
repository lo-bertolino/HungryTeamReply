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


class LocusBase:
    def __init__(self):
        pass

    def __repr__(self):
        return '%s:%s' % (self.__class__, self.__dict__)

    def __str__(self):
        return repr(self)

    def signature(self):
        return "?"

    def update(self, winner, looser):
        raise NotImplementedError

    def get(self, mode='sample'):
        raise NotImplementedError

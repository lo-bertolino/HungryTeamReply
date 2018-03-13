# -*- coding: utf-8 -*-
###########################################################################
#             #                                                           #
#   #####     #  euLOGy v0.1 -- Copyright © 2018 Giovanni Squillero       #
#  ######     #  http://staff.polito.it/giovanni.squillero/               #
#  ###   \    #  giovanni.squillero@polito.it                             #
#   ##G  c\   #                                                           #
#   #     _\  #  This code is licensed under a BSD 2-clause "simplified"  #
#   |  _/     #  license -- see the file LICENSE.md for details.          #
#             #                                                           #
###########################################################################

"""euLOGy

Copyright © 2017, Giovanni Squillero.
Licensed under a BSD 2-clause "simplified" license -- see LICENSE.md
"""

import sys
import logging
from .setup import init_logging
from .utilities import traceall

assert sys.version_info >= (3, 4)

# copy some constants...
CRITICAL = logging.CRITICAL
CRITICAL_RAW = CRITICAL + 1
ERROR = logging.ERROR
ERROR_RAW = ERROR + 1
WARNING = logging.WARNING
WARNING_RAW = WARNING + 1
INFO = logging.INFO
INFO_RAW = INFO + 1
DEBUG = logging.DEBUG
DEBUG_RAW = DEBUG + 1
NOTSET = logging.NOTSET
NOTSET_RAW = NOTSET + 1

if not logging.getLogger().hasHandlers():
    # root logger not yet initialized, let's take control
    init_logging()

logging.traceall = traceall

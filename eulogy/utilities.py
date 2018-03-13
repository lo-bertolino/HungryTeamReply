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

import logging

def traceall(msg, *args, **kwargs):
    logging.log(1, msg, *args, **kwargs)

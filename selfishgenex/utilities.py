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

import numpy


def compact_list(arg):
    plist = [(1, _) for _ in arg]

    i = 0
    while i < len(plist)-1:
        if plist[i][1] == plist[i+1][1]:
            new = (plist[i][0]+plist[i+1][0], plist[i][1])
            plist = plist[:i] + [new] + plist[i+2:]
        else:
            i += 1

    fmt = "{}×{}"
    for _, e in plist:
        if len(str(e)) > 1:
            fmt = "{} × {}"

    dlist = list()
    for m, e in plist:
        opt1 = " ".join([str(e)] * m)
        opt2 = fmt.format(m, str(e))
        if len(opt1) <= len(opt2):
            dlist += [str(e)] * m
        else:
            dlist.append(fmt.format(m, str(e)))
    return dlist


def describe_list(arg):
    return ", ".join(compact_list(arg))


def plural(tag, num):
    if num == 1:
        return tag

    if tag[-1] in "sxz":
        tag += "es"
    elif tag[:-2] in ["ch", "sh"]:
        tag += "es"
    elif tag[-2] not in "aeiou" and tag[-1] == "y":
        tag = tag[:-1] + "ies"
    else:
        tag += "s"
    return tag

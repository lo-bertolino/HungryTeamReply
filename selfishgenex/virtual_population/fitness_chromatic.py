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


class FitnessChromatic(Fitness):
    """A fitness implementing "Chromatic Selection", a fast, simple and
    grossly approximate technique for tackling multi-value optimization
    (not completely unrelated to "Lexicase Selection"). Reference: "Chromatic
    Selection – An Oversimplified Approach to Multi-objective Optimization"
    by G. Squillero (DOI: 10.1007/978-3-319-16549-3_55)"""

    def __lt__(self, other):
        # Standard lexicographic
        if not other:
            return False
        elif not self:
            return True
        return tuple(self) < tuple(other)

""" MEMO

# coding: utf-8

# In[1]:


import numpy as np


# In[31]:


i1 = (0, 0, 1)
i2 = (1, 2, 2)


# In[34]:


population = np.array([i1, i2])
diff = ((population[0] - population[1]) / population.sum(axis=0))
print("d=", population.max(axis=0) - population.min(axis=0))
print("rd=", diff)
probabilities = diff / diff.sum()
print("p=", probabilities)
c = np.choose(range(l))


# In[36]:


population.


# In[ ]:


population.


# In[ ]:


np.max(a, axis=0)

"""
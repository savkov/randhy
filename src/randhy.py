# This file is part of randhy.
#
# randhy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# randhy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with randhy.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Aleksandar Savkov'

import random


def _shuffle(a, b):
    """

    :param a: vector a
    :param b: vector b
    :return: shuffled vectors
    """
    sha, shb = range(len(a)), range(len(a))
    for i in range(len(a)):
        if random.choice([True, False]):
            sha[i], shb[i] = b[i], a[i]
        else:
            sha[i], shb[i] = a[i], b[i]
    return sha, shb


def randhy_test(a, b, y, k, delta_t):
    """

    :param a: first predicted label vector
    :param b: second predicted label vector
    :param y: true label vector
    :param k: number of iterations
    :param delta_t: evaluation function
    :return: proportion of iteration that supported the hypothesis
    """

    r = 0

    delta_t_score = delta_t(a, b, y)

    for i in range(k):
        sha, shb = _shuffle(a, b)
        if delta_t(sha, shb, y) >= delta_t_score:
            r += 1
    return (r + 1.0) / (k + 1.0)
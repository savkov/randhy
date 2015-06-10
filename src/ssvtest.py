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

import pandas as pd
from randhy import randhy_test
from bioeval import evaluate
from ssvutils import SSVList, ssv2set
from itertools import combinations

names = sorted(['ark', 'ritter', 'irc', 'genia', 'svmt', 'stanford', 'ctakes', 'rasp', 'wapiti', 'nopos'])
jobs = ['bnlp_top', 'bnlp_top_cveval', 'bnlp_top_yamcha', 'bnlp_top_beiso']


def fscore(ssv):
    f1, _, _ = evaluate(*ssv2set(ssv))
    return f1


def delta_fscore(a, b, *args, **kwargs):
    ssv_a = SSVList([x for y in a for x in y])
    ssv_b = SSVList([x for y in b for x in y])
    fsc_a = fscore(ssv_a)
    fsc_b = fscore(ssv_b)
    return abs(fsc_a - fsc_b)


def test(fp1, fp2, k=100000):
    a = SSVList()
    a.parse_file(fp1, cols='chunkg', tab_sep='\t')
    b = SSVList()
    b.parse_file(fp2, cols='chunkg', tab_sep='\t')

    aseq = a.sequences
    bseq = b.sequences

    if len(aseq) > len(bseq):
        aseq = aseq[:len(bseq)]
    elif len(aseq) < len(bseq):
        bseq = bseq[:len(aseq)]

    return randhy_test(aseq, bseq, None, k, delta_fscore)


def test_job(job, k=10000):
    results = {}
    c = combinations(range(len(names)), 2)
    for cc in c:
        key = (names[cc[0]], names[cc[1]])
        if key not in results.keys():
            fp1 = '/home/sasho/Experiments/%s/%s/1/output.data' % (job, key[0])
            fp2 = '/home/sasho/Experiments/%s/%s/1/output.data' % (job, key[1])
            results[key] = test(fp1, fp2, k)
            print (names[cc[0]], names[cc[1]]), 'done'
    return results


def test_job_pair(job1, job2, k=10000):
    results = {}
    for n in names:
        fp1 = '/home/sasho/Experiments/%s/%s/1/output.data' % (job1, n)
        fp2 = '/home/sasho/Experiments/%s/%s/1/output.data' % (job2, n)
        results[n] = test(fp1, fp2, k)
        print job1, job2, n, 'done'
    return results


def make_table(results):
    tab = []
    for n1 in names:
        row = []
        for n2 in reversed(names):
            k = (n1,n2)
            if n1 == n2 or k not in results.keys():
                row.append(None)
                continue
            row.append(results[k])
        tab.append(row)
    return pd.DataFrame(tab, index=names, columns=list(reversed(names)))[list(reversed(names))[:-1]][:-1]


if __name__ == '__main__':
    a = SSVList()
    a.parse_file('/home/sasho/Experiments/bnlp_top/ark/1/output.data', cols='chunkg', tab_sep='\t')
    b = SSVList()
    b.parse_file('/home/sasho/Experiments/bnlp_top/ritter/1/output.data', cols='chunkg', tab_sep='\t')

    print randhy_test(a.sequences, b.sequences, None, 10, delta_fscore)

    # for ca, cal in zip(cs, al):
    #     print len(cal), ca, cal
import pytest
import random

import spacy
import thinc.extra.datasets


IMDB_DOCS_LEN = 2


def imdb_docs():
    data, _ = thinc.extra.datasets.imdb()
    return [x for x, _ in data[:IMDB_DOCS_LEN]]


def choice():
    return random.choice([True, False])


def random_variation(tags):
    return ['VERB' if t == 'NOUN' and choice() else t for t in tags]


random.seed(1984)
nlp = spacy.load('en_core_web_sm')
text = ' '.join(imdb_docs()).replace('\n', ' ')
doc = nlp(text)
_gold = [(i, t.pos_) for i, t in enumerate(doc)]
_o_a = random_variation(_gold)
_o_b = random_variation(_gold)


def precision(a, b):
    tp = len(set(a) & set(b))
    return tp / len(set(a))


def recall(a, b):
    tp = len(set(a) & set(b))
    return tp / len(set(b))


def f1(a, b):
    pr = precision(a, b)
    re = recall(a, b)
    return 2 * (pr * re / (pr + re))


def f1_delta(a, b, gold):
    f1_a = f1(a, gold)
    f1_b = f1(b, gold)
    return abs(f1_a - f1_b)


@pytest.fixture(scope='session')
def o_a():  # observations A
    return _o_a


@pytest.fixture(scope='session')
def o_b():  # observations B
    return _o_b


@pytest.fixture(scope='session')
def gold():  # gold labels
    return _gold


@pytest.fixture(scope='session')
def t():
    return f1_delta

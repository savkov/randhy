import randhy


def test_random_swap(o_a, o_b):
    swapped_a, swapped_b = randhy.random_swap(o_a, o_b)
    # make sure the new vectors are the same length
    assert len(swapped_a) == len(swapped_b) == len(o_a) == len(o_b)
    # make sure we are not losing data
    for pair, a, b in zip(zip(swapped_a, swapped_b), o_a, o_b):
        assert a in pair and b in pair
        if pair[0] != pair[1]:
            assert a != b


def test_resampling():
    a = list(range(10))
    b = list(range(10, 20))
    a_, b_ = randhy.resample(a, b)
    assert all([0 <= x < 20 for x in a_])
    assert all([0 <= x < 20 for x in b_])
    assert len(a) == len(a_)
    assert len(b) == len(b_)
    assert a_ != b_


def test_random_test(o_a, o_b, gold, t):
    p = randhy.random_test(o_a, o_b, gold, t)
    assert isinstance(p, float)
    assert p > 0.05


def test_paired_randomisation_tes(o_a, o_b, gold, t):
    p = randhy.paired_randomisation_test(o_a, o_b, gold, t)
    assert isinstance(p, float)
    assert p > 0.05

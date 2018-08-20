# randhy
_Hypothesis thesting with approximate randomisation_

[![CircleCI](https://circleci.com/gh/savkov/randhy.svg?style=svg&circle-token=ff0102ad2d043f5548279e8f48a5fcde2297978b)](https://circleci.com/gh/savkov/randhy)
[![Maintainability](https://api.codeclimate.com/v1/badges/c21544109986302622de/maintainability)](https://codeclimate.com/github/savkov/randhy/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c21544109986302622de/test_coverage)](https://codeclimate.com/github/savkov/randhy/test_coverage)

Approximate randomisation is a significance testing approach suitable for NLP
problems.

### 🤔 Why not a traditional t-test?

While randomisation tests are just as good as analytical approaches such as the 
_t-test_, they are better when the assumptions of the latter are not met and
they are also quite simple to implement.

### 🖥️ Installation

```bash
pip install randhy
```

### References

1. _[William Morgan, Statistical Hypothesis Tests for NLP - Stanford Computer Science (slides)](https://cs.stanford.edu/people/wmorgan/sigtest.pdf)_
2. _[Wassily Hoeffding. 1952. The Large-Sample Power of Tests Based on Permutations of Observations. Annals ofMathematical Statistics, 23, 169–192.](https://www.jstor.org/stable/2958014?seq=1#page_scan_tab_contents)_
3. _[Eric W. Noreen. 1989. Computer Intensive Methods forTesting Hypothesis. John Wiley & Sons](https://www.amazon.co.uk/Computer-Intensive-Methods-Testing-Hypotheses-Introduction/dp/0471611360)_

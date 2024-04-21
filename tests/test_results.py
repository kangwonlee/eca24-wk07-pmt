'''
Unit tests for pmf assignment

'''

import math
import pathlib
import random
import sys

from typing import Dict, Tuple


import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(
    0,
    str(proj_folder)
)


import wk08


random.seed()


import pytest
import random 
from wk08 import wk08


PMF = Dict[int, float]

# Fixture to generate a randomized PMF for testing
@pytest.fixture
def random_pmf() -> PMF:
    num_outcomes = random.randint(3, 8)  # Ensure a reasonable number of outcomes
    pmf = {}
    remaining_prob = 1.0
    for i in range(num_outcomes - 1):
        prob = random.uniform(0.05, 0.3)  # Adjust probability ranges if needed
        pmf[i] = prob
        remaining_prob -= prob
    pmf[num_outcomes - 1] = remaining_prob  # Assign the last outcome
    return pmf


# Fixture to generate random bounds
@pytest.fixture
def random_bounds(random_pmf:PMF) -> Tuple[float, float]:
    max_key = max(random_pmf.keys())  # Extract the maximum key from the PMF
    return random.randint(0, max_key), random.randint(0, max_key)  


# Typical Test Cases
def test_wk08_single_outcome(random_pmf:PMF, random_bounds:Tuple[float, float]):
    lower, upper = random_bounds
    if lower > upper:  # Ensure lower bound is not greater than upper bound
        lower, upper = upper, lower
    result = wk08(random_pmf, lower, upper)
    assert 0 <= result <= 1  # Probability should be within the valid range


def test_wk08_full_range(random_pmf:PMF):
    lower = min(random_pmf.keys())
    upper = max(random_pmf.keys())
    result = wk08(random_pmf, lower, upper)
    assert math.isclose(result, 1.0)  # Probability of the entire range should be 1


def test_wk08_custom_pmf():
    pmf = {0: 0.3, 1: 0.2, 2: 0.4, 3: 0.1}
    result = wk08(pmf, 1, 3)
    assert math.isclose(result, 0.7)


if "__main__" == __name__:
    pytest.main([__file__])

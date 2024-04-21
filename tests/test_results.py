'''
Unit tests for pmf assignment

'''

import math
import pathlib
import random
import sys

from typing import Dict, Tuple


import numpy as np
import numpy.random as nr
import numpy.testing as nt
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


@pytest.fixture
def expected_output() -> float:
    return random.uniform(0.01, 0.99)


@pytest.fixture
def max_key() -> int:
    return random.randint(5, 20)


# Fixture to generate random bounds
@pytest.fixture
def random_bounds(max_key:int) -> Tuple[float, float]:
    lower = random.randint(0, max_key//2)
    upper = random.randint(lower + 1, max_key)
    return lower, upper


# Fixture to generate a randomized PMF for testing
@pytest.fixture
def random_pmf(expected_output:float, max_key:int, random_bounds:Tuple[float, float]) -> PMF:
    lower, upper = random_bounds

    salt_pepper = nr.uniform(size=(upper - lower + 1))
    salt_pepper *= (expected_output/np.sum(salt_pepper))

    salt_pepper_rest = nr.uniform(size=(max_key - len(salt_pepper) + 1))
    salt_pepper_rest *= ((1.0 - expected_output)/np.sum(salt_pepper_rest))

    assert len(salt_pepper) + len(salt_pepper_rest) == max_key + 1

    pmf_array = np.hstack([salt_pepper_rest[:lower],salt_pepper, salt_pepper_rest[lower:]])

    assert len(pmf_array) == max_key + 1
    nt.assert_almost_equal(np.sum(pmf_array), 1.0)

    pmf = {}

    for k, v in enumerate(pmf_array):
        pmf[k] = v

    for k in range(lower, upper+1):
        assert k in pmf
        assert pmf[k] == salt_pepper[k-lower]

    return pmf


@pytest.fixture
def random_pmf_txt(random_pmf:PMF) -> str:
    return "\n".join([f"{k:2d} : {v:.4f}" for k, v in random_pmf.items()])


# Typical Test Cases
def test_wk08_single_outcome(random_pmf:PMF, random_bounds:Tuple[float, float], random_pmf_txt:str):
    lower, upper = random_bounds
    if lower > upper:  # Ensure lower bound is not greater than upper bound
        lower, upper = upper, lower
    result = wk08(random_pmf, lower, upper)
    assert 0 <= result <= 1, f"{random_pmf_txt}\nresult = {result:f}" # Probability should be within the valid range


def test_wk08_full_range(random_pmf:PMF, random_pmf_txt:str):
    lower = min(random_pmf.keys())
    upper = max(random_pmf.keys())
    result = wk08(random_pmf, lower, upper)
    assert math.isclose(result, 1.0), f"{random_pmf_txt}\nresult = {result:f}"  # Probability of the entire range should be 1


def test_wk08_custom_pmf(random_pmf:PMF, random_bounds:Tuple[int, int], expected_output:float, random_pmf_txt:str):
    lower, upper = random_bounds
    result = wk08(random_pmf, lower, upper)
    assert math.isclose(result, expected_output), (
        f"{random_pmf_txt}\n"
        f"result = {result:f}\n"
        f"expected_output = {expected_output:f}"
    )


if "__main__" == __name__:
    pytest.main([__file__])

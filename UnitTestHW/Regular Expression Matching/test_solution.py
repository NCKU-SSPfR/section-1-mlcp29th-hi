import pytest
from solution import Solution
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

@pytest.mark.parametrize("s, p, expected_res", testcases)
def test_solution(s, p, expected_res):
    solution = Solution()
    assert solution.isMatch(s, p) == expected_res

@pytest.mark.xfail
def test_broken_solution():
    solution = Solution()
    assert solution.isMatch("a", ".*.")

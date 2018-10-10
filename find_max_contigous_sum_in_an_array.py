import pytest
@pytest.fixture(params=[
        ((-2, 1, -3, 4, -1, 2, 1, -5, 4), 6),
        ((-5, 6, 7, 1, 4, -8, 16), 26),
    ]
)
def max_array_sum(request):
    return request.param

def test_max_contigous_sum(max_array_sum):
    arr, max_sum = max_array_sum
    assert find_max_contigous_sum(arr) == max_sum, 'incorrect max contigous sum'


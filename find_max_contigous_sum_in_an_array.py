import pytest

def find_max_contigous_sum(arr):
    max_sum = 0
    for index,_ in enumerate(arr):
        cur_sum = 0
        for item in arr[index:]:
            cur_sum += item
            max_sum = cur_sum > max_sum and cur_sum or max_sum
            print("index: ", index, "item:", item, "max: ", max_sum, "cur: ", cur_sum)
    return max_sum


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

def test_kadane_max_subarray(max_array_sum):
    arr, max_sum = max_array_sum
    assert kadane_max_subarray(arr) == max_sum, 'incorrect max contigous sum'

from base import Solution

class AlgoLoHi(Solution):
    def search_last_true(self, array: list) -> int:
        lo, hi = 0, len(array)
        while lo < hi:
            mid = (hi + lo) // 2
            if array[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


if __name__ == '__main__':
    array = [True, False, False, False, False, False]
    obj = AlgoLoHi()
    print("Hi")
    assert obj.search_last_true(array) == 0

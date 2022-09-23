"""
Find the major position of True
Limitations:
"""

from base import Solution

class MyComplicateAlgorithm(Solution):
    def search_last_true(self, array: list):

        def get_next_index(array, cur_index, crumbs, step_up):
            next_index = 0
            step = 0
            if step_up:
                if cur_index == len(array) - 1:
                    return cur_index
                step = (len(array) - cur_index) // 2
                step = step if step else 1
            else:
                if cur_index == 0:
                    return cur_index
                step = -(cur_index // 2)
                step = step if step else -1
            next_index = cur_index + step
            if crumbs[next_index]:
                return cur_index
            crumbs[next_index] = True
            return next_index

        crumbs = []
        for i in range(len(array)):
            crumbs.append(False)
        assert len(crumbs) == len(array)
        index = len(array) - 1
        result = -1
        next_index = 0
        step_up = False
        while True:
            step_up = True if array[index] else False
            if array[index]:
                result = max(result, index)
            next_index = get_next_index(array=array, cur_index=index, crumbs=crumbs, step_up=step_up)
            if next_index == index:
                break
            index = next_index
        return result

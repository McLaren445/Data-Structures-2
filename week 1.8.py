#First & Last Position
def search_range(nums: list[int], target: int) -> tuple[int, int]:
    def find_left():
        lo, hi = 0, len(nums) - 1
        idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                idx = mid        # record
                hi = mid - 1     # but keep searching left
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return idx
    def find_right():
        lo, hi = 0, len(nums) - 1
        idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                idx = mid        # record
                lo = mid + 1     #but keep searching right
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return idx

    return (find_left(), find_right())
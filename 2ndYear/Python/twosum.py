class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a hash map to store value: index
        prev_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            # If the complement is in the map, we found the pair
            if diff in prev_map:
                return [prev_map[diff], i]
            # Otherwise, add current number to map
            prev_map[n] = i

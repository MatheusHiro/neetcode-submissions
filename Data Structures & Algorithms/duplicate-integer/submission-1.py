class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = []
        for i, n in enumerate(nums):
            if n in lookup:
                return True
            lookup.append(n)
        
        return False
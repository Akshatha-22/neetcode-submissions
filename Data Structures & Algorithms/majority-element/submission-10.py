class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = Counter(nums)
        n = len(nums)

        for i in result:
            if result[i] > n/2:
             return i
        
        return majorityElement
        
        
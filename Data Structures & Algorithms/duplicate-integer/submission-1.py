class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = Counter(nums)

        for i in result:
            if result[i] > 1:
                return True
        return False
    print(hasDuplicate)    
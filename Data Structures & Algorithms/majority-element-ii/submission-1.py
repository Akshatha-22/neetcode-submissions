class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = Counter(nums)
        n = len(nums)

        new_list = []

        for i in result:
            if result[i] > n/3:
                 new_list.append(i)
        return new_list
            
            
            
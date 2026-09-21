class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       res_1 = ''.join(sorted(s))
       res_2 = ''.join(sorted(t))

       return res_1 == res_2
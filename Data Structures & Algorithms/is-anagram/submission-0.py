class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       res_1 = ''.join(sorted(s))
       res_2 = ''.join(sorted(t))

       if res_1 == res_2:
          return True
        
       return False   
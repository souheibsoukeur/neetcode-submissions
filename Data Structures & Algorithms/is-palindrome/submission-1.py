import re  # Moved to the top level

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = re.sub(r"\s*?|[^\w]", "", s.lower()) 
        j = len(alphanum) - 1 
        end = j // 2 -1 
        print(alphanum)
        for char in alphanum: 
            if char != alphanum[j]: 
                return False
            j -= 1
            if j == end : break 
             
            
                
        return True  # Now correctly inside the function block

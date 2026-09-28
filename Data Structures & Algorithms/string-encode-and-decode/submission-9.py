from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] 
        for s in strs : 
            res.append(f"{len(s)}#{s}") 
        return "".join(res) 
        
    def decode(self, s: str) -> List[str]:
        resp= []
        i = 0 
        while i < len(s):
            j = s.find("#" , i) 
            l= int(s[i:j]) 
            resp.append(s[j+1:j+1+l]) 
            i=j+l+1
        return resp
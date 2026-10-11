class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dumped= set(nums) 
        maxx = 0 
        
        for n in nums : 
            if (n-1) not in dumped : 
                current=1 
                while(n+current) in dumped : 
                    current +=1 
                maxx = max(maxx,current) 
        return maxx 
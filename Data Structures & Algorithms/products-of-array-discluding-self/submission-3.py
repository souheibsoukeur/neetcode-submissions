class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        pp = [1] * (n+1) 
        sp = [1] * (n+1) 
        for  i in range(n) : 
            pp[i+1] = pp[i] * nums[i] 
            sp[n-1-i]= sp[n-i] * nums[n-i-1]  
        new=[]
        for i in range(n) :
            new.append(pp[i] * sp[i+1])
        return new 
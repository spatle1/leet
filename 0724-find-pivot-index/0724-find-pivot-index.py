class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right=0 ,sum(nums)
       

        for i,ele in enumerate(nums):
            right-=ele
            if left==right:
                return i
            left+=ele
        return -1 
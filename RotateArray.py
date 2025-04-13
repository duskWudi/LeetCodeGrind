class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def rev(start, end, nums):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1
        
        n = len(nums)
        k %= n
        rev(0, n-1, nums)
        rev(0, k-1, nums)
        rev(k, n-1, nums)
        

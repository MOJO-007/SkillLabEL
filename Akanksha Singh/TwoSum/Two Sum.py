class Solution:
    def twoSum(self, nums, target):
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i 
    
        return None

# driver code
solution = Solution()
nums = [1,2,3,4,5]
target = 9
print(solution.twoSum(nums, target))
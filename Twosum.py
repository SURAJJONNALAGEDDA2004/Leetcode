class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        a=len(nums)
        for i in range(0,a):
            for j in range(i+1,a):
                b=nums[i]+nums[j]
                if(b==target):
                    l.append(i)
                    l.append(j)
        return l

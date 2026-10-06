class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            if(hash_map.get(target - nums[i]) != None):
                return[hash_map.get(target - nums[i]), i]
            
            hash_map[nums[i]] = i
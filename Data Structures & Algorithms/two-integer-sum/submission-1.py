class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # indices = {}

        # for i in range(len(nums)):
        #     indices[nums[i]] = i
        
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]]
        # return []

        # for i, n in enumerate(nums):
        #     indices[n] = i

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]]
        # return []

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in indices:
        #         return [indices[diff], i]
        #     indices[n] = i
        
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []       



        
                

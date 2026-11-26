class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1

        # res = []
        # while len(res) < k:
        #     top = max(count, key = count.get)
        #     res.append(top)
        #     del count[top]
        # return res

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()
        # res = []
        # while len(res) < k:
        #     top = arr.pop()[1]
        #     res.append(top)
        # return res

        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) +  1
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        






        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
from collections import Counter

class Solution:
    def topKFrequent(self, nums: 'list[int]', k: int) -> 'list[int]':
        freq_count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for key, v in freq_count.items():
            buckets[v].append(key)
        
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for r in buckets[i]:
                result.append(r)
                if len(result) == k:
                    return result
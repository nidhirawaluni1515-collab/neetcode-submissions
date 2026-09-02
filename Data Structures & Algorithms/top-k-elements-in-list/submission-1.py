class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            res = []
            bucket = [[] for _ in range(len(nums)+1)]
            for n in nums :
                count[n] = count.get(n,0) + 1
            for key ,value in count.items():
                    bucket[value].append(key) 
            for i in range(len(bucket) - 1 , 0 , - 1 ) :
                if bucket[i] :
                      for p in bucket[i] :
                            res.append(p)
                            if len(res) == k :
                                return res
        
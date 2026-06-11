class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aux = dict()
        for i, n in enumerate(nums):
            if n not in aux:
                aux[n] = 1
            else:
                aux[n] = aux[n] + 1
            
        sortedD = dict(sorted(aux.items(), key=lambda x: x[1]))
        return list(sortedD)[-k:]
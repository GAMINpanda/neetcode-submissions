class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts: Dict = {}
        for value in nums:
            if value in numCounts:
                numCounts[value] += 1
            else:
                numCounts.update({value : 1})

        largestKeys = []

        while(len(largestKeys) < k):
            largest = 0
            largestKey = None
            
            for key, value in numCounts.items():
                if value > largest:
                    largest = value
                    largestKey = key

            numCounts.pop(largestKey)
            largestKeys.append(largestKey)

        return largestKeys
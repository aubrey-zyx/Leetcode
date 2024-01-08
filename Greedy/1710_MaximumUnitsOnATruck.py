class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        i = 0
        res = 0
        while truckSize and i < len(boxTypes):
            boxes = min(truckSize, boxTypes[i][0])
            res += boxes * boxTypes[i][1]
            truckSize -= boxes
            i += 1
        return res
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                ht[stack.pop()] = num
            stack.append(num)

        return [ht.get(num, -1) for num in nums1]
class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zero = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.non_zero[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, num in vec.non_zero.items():
            if i in self.non_zero:
                res += num * self.non_zero[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
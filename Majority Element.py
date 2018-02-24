import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = 0
        self.assertEqual(Solution().majorityElement(Input),Output)
    def testSample(self):
        Input = [1,1,2]
        Output = 1
        self.assertEqual(Solution().majorityElement(Input),Output)

class Solution():
    def majorityElement(self, nums):
        if nums == []:
            return 0
        nums.sort()
        k = int(len(nums)/2)
        return nums[k]

if __name__ == '__main__':
    unittest.main()

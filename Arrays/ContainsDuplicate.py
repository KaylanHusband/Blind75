class Solution:
    """
    Link: https://leetcode.com/problems/contains-duplicate
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 1: Sorting - When the elements are sorted, we just need to check if 
                    the previous element equals the current. If so, the deuplicate is 
                    found
        Complexity Analysis:
        Time: O(nlgn)
        Space: O(1)
        """
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 2: Using HashSet - Each time we iterate though the array, 
                    we need to check if the element aleady exists in the set.
                    If so, then we have found the duplicate. Checking if an element is in the set
                    is O(1) on average, so this will not increase the time complexity.
        Complexity Analysis:
        Time: O(n)
        Space: O(n)
        """
        checkSet = set([])
        for n in nums:
            if n in checkSet:
                return True
            checkSet.add(n)
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 3: Same as approach 2, except just one line
        Complexity Analysis:
        Time: O(n)
        Space: O(n)
        """
        return len(nums) != len(set(nums))
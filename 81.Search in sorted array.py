class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right =0, len(nums)-1
        while left <= right:
            mid = (left + right )//2
            if nums[mid]==target:
                return True
            if nums[left] < nums[mid] and target >= nums[left] and target < nums[mid]:
                right = mid-1
            elif nums[mid]<nums[right] and target > nums[mid] and target <= nums[right]:
                left = mid+1
            else:
                return target in nums[left:right+1]
        return False
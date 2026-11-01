class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        temp = []
        while (i < m) and (j < n):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
    
            elif nums2[j] <= nums1[i]:
                temp.append(nums2[j])
                j += 1
                
        if i < m:
            temp.extend(nums1[i:m])
        if j < n:
            temp.extend(nums2[j:])
        for i in range(len(temp)):
            nums1[i] = temp[i]
        

        
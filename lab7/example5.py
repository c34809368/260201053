numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
nums1=set(numbers1)
nums2=set(numbers2)
intersection=set()
for i in nums1:
  if i in nums2:
    intersection.add(i)
nums1.update(nums2)
print("Intersection set of the sets is:",intersection)
print("Union of two sets is:",nums1)
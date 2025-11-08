nums = [1,2,3,4,5,6,1,2,3,8]
d1 = {}
for i in range (len(nums)):
    if nums[i] in d1:
        d1[nums[i]] += 1
    else:
        d1[nums[i]] = 1
print(d1)
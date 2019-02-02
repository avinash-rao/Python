
print("Enter the numbers: ")
nums = []
n = 0           # to store the length of nums
while True:
    num = input()
    if num == '':
        break
    nums.append(int(num))
    n += 1

nums.sort()

# Find out mean
mean = sum(nums)/n

# Find out median
if n % 2 == 0:              #If total number of elements is even
    median = (nums[(n//2)-1] + nums[n//2])/2
else:                       #If total number of elements is odd
    median = nums[n//2]

# Find out mode
tupleNums = tuple(nums)
mode = tupleNums[0]
for i in tupleNums:
    if nums.count(i) > mode:
        mode = i

# Display M3

print(mean)
print(median)
print(mode)
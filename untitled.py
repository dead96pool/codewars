
nums = [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1]
count = {1:0, 2: 0}


for i in range(len(nums)):
    
    if nums[i] == 1:
        print("i:", i)
        if (i == 0 or nums[i-1] == 0) and (i == len(nums) - 1 or nums[i+1] == 0):
            print("i:", i)
            count[1] += 1
        elif nums[i+1] == 1:
            print("i:", i)
            size = 1
            while nums[i+size] == 1 or (size > 2 and nums[i-1] == 1):
                print("i", i, " size:", size)
                size += 1
            if size in count:
                count[size] += 1

print(count) 
def histogram(nums):
    for i in nums:
        for j  in range(i):
            print("*", end = "")
        print()
     
histogram([4, 6 ,7])
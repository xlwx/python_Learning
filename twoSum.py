def twoSum(nums,target):
	h = {}
	for i,v in enumerate(nums):
		if target - v in h:
			return (h[target-v],i)
		h[v] = i

if __name__ == '__main__':
	nums = [2,3,4,2,2]
	res = twoSum(nums,4)
	print(res)




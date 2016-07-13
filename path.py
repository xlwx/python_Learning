import os 

# define a map that stores the key words and its related relative path
map = {}

def findPath(key,d):
	for x in os.listdir(d):
		#need abs path for .isdir() and .isfile()
		path=os.path.join(d,x)

		if os.path.isdir(path):
			findPath(key,path)
		elif os.path.isfile(path):
			if key in x:
				#could print out here or write into the disc
				map[x] = path 
		else:
			pass

if __name__ == '__main__':

	key = input('Please input the key words-->')
	#path = input('Please input the root path-->')
	d = '.'
	print('The root path is : %s' % os.path.abspath('.'))

	findPath(key,d)

	for key in map:
		print('%s: %s' % (key,map[key]))

	print('End Searing...')
import sys

def decrypt(encryption):
	lst = []
	points = 0
	for i in encryption:
		if i!='.':
		    lst.append(i)
		    points = 0
		    continue
		
		points +=1
		if points == 2 and lst:
			lst.pop()
			points = 0
	return ''.join(lst)


if __name__ == '__main__':
	data = sys.stdin.read()
	d = decrypt(data)
	print(d)

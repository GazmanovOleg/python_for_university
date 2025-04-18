import sys
#ls -l | python3 task2.py
def get_mean_size(output):
	sum_file = 0
	count = 0
	for l in output:
		count+=1
		sum_file+=int(l.split()[4])
	return sum_file / count
	
if __name__ == '__main__':
	data = sys.stdin.readlines()[1:]
	if not data:
		print('directory is empty')
	else:
		mean_size = get_mean_size(data)
		print(f'Average file size is {mean_size} bytes')
    

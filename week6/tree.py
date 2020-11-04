from pathlib import Path
import os
import sys
#Part B
#2
def print_as_tree1(path):
	if not path.is_dir():
		sys.stderr.write("Not valid path:\n")
		return
	for p in sorted(path.glob('**/*')):
		if p.is_dir():
			print(' '*len(p.parts), 'D ', p.name)
		else:
			print(' '*len(p.parts), 'F ', p.name)
#2 This solution is not perfect, but it's to try
def print_as_tree2(path):
	first = True
	str_len = 0;
	firt_folder = True
	if not path.is_dir():
		sys.stderr.write("Not valid path:\n")
		return
	for p in sorted(path.glob('**/*')):
		count_slash = str(p.parent).count('/')
		if p.is_dir():
			if len(list(p.iterdir())) != 0 and firt_folder:
				print(' ', 'D ', p.name, end ='')
			else:
				print(' '*len(str(p.parent)), 'D ', p.name)
				first = False
				firt_folder = False
		else:
			if first:
				print(' ', 'F ', p.name)
				str_len = len(p.name)
				first = False
			else:
				if(len(p.parts) != 1):
					print(' '*(len(str(p.parent))+str_len-2*count_slash), 'F ', p.name)
				else:
					print(' ', 'F ', p.name)


def main():
 	#print_as_tree1(Path('.'))
 	print_as_tree2(Path('.'))
 	

if __name__ == '__main__':
 	main()
 	
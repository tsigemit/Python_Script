from pathlib import Path
import sys
#Part A
def find_path(path, wildcard):
	if not path.is_dir():
		sys.stderr.write("Not valid path:\n")
		return

	if '/' in wildcard:
		sys.stderr.write("Remove / from the wildcard:\n")
		return 

	for p in path.glob('**/'+wildcard):
		print(p)
# part B
def print_dir(depth, path):
	if not path.is_dir():
		sys.stderr.write("Not valid path:\n")
		return
	for p in sorted(path.iterdir()):
		if p.is_dir():
			print(' '*depth, 'D ', p)
		else:
			print(' '*depth, 'F ', p)

def main():
	path=Path(sys.argv[1])
	wildcard=sys.argv[2]
	print('\nPart_A')
	find_path(path, wildcard)
	print('\nPart_B')
	print_dir(4, Path('.'))
if __name__ == '__main__':
 	main()
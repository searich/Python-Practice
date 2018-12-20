from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}')

#in_file = open(from_file)
indata = open(from_file).read()

print(f'The input file is {len(indata)} bytes long')

print(f'Does the output file exist? {exists(to_file)}')
print('Redy, hit return to continue, ctrl-c to abort.')
input()

open(to_file, 'w').write(indata)
#out_file.write(indata)

print('Allright, all done!')

#out_file.close()
#in_file.close()
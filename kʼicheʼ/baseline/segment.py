import sys 
from ATT import ATTFST

a = ATTFST(sys.argv[1])

for line in sys.stdin.readlines():
	row = line.strip().split('\t')

	output = []
	for token in row[0].split(' '):
		segs = a.apply(token)
		max_seg = ''
		for seg in segs:
			max_seg = seg
			break
		if max_seg:
			output.append(max_seg[0].strip('>'))
		else:
			output.append(token)
			
	print('%s\t%s' % (row[0], ' '.join(output)))	

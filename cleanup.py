from sys import argv


f = open("output_pi%s.txt" % (argv[1]) ,"r").readlines()
rows = []
for line in f:
	try:
		line = line.split(' ')
		result =  'pi%s' % argv[1] , line[1], line[2], line[12][3:-1], line[-1][5:-1]
	except:
		result = ''

	print ' '.join(result)

import csv 
import sys 

uniqlines = set(open(sys.argv[1]).readlines())

with open(sys.argv[2],'w', newline='\n') as out:
	writer = csv.writer(out, delimiter=',', quotechar='"', lineterminator='\n')
	writer.writerow([sys.argv[3], 'Valid', 'creationTime', 'lastModifiedTime', 'count'])
	for line in uniqlines:
		line = line.strip()
		writer.writerow([line, 'True','4 Mar 2016 10:21:22 NZDT','4 Mar 2016 10:21:22 NZDT','1'])

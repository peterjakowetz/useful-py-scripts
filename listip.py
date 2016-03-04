import netaddr 
import csv
import sys

example = netaddr.IPSet([str(sys.argv[1])])

with open(str(sys.argv[2]),'w', newline='') as out:
	writer = csv.writer(out, delimiter=',', quotechar='"')
	writer.writerow(['Address', 'Customer', 'Remark', 'creationTime', 'lastModifiedTime', 'count'])
	for ip in example:
		writer.writerow([ip, (sys.argv[3]), 'Trusted MTA','2 Mar 2016 14:21:22 NZDT','2 Mar 2016 14:21:22 NZDT','1'])

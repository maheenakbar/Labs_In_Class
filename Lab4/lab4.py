import re

file_name = open('mbox-short.txt')
#nums1 = list()

for line in file_name:
	line = line.strip()
	#if re.search('^From', line):
	#print (line)
	nums1 = re.findall('^From', line)
	nums2 = re.findall('^From.*([0-9])', line)
print (nums1)
print (nums2)
	
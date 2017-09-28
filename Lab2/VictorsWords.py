victor = "TheVictors.txt"

try:
	victor_text = open(victor)
except:
	print ("This file cannot be opened", victor)
	exit()

count = {}
for line in victor_text:
	line = line.rstrip()
	words = line.split()
	for word in words:
		if word not in count:
			count[word] = 1
		else:
			count[word] += 1

count_tuple = list()
for key, value in count.items():
	count_tuple.append((value, key))

count_sorted = sorted(count_tuple, reverse = True)

for value, key in count_sorted[:15]:
	print (key, value)



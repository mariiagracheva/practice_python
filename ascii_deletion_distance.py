# ASCII deletion distance between two words
# cat - at = 99

def ascii_del_dist(str1, str2):
	res = 0
	comm1 = []
	comm2 = []
	for i in range(len(str1)):
		if str1[i] in str2:
			comm1.append(str1[i])
		else:
			res = res + ord(str1[i])

	for j in range(len(str2)):
		if str2[j] in comm1:
			comm2.append(str2[j])
		else:
			res = res + ord(str2[j])

	print comm1, comm2
	return res



print ascii_del_dist('cat', 'at')
print ascii_del_dist('boat', 'got')
print ascii_del_dist("thought", "sloughs")
# print ord('b'), ord('a'), ord('g')
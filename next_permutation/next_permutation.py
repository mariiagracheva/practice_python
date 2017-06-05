def next_perm(str):

	# Find longest non-increasing suffix
	# if len(str) < 2:
	# 	return str

	i = len(str)-1

	while ( i > 0 and str[i-1] >= str[i]):
		i = i - 1
	# print i
	#  Are we at the last permutation already?
	if (i <= 0):
		return str

	# Let array[i - 1] be the pivot
	# Find rightmost element that exceeds the pivot
	j = len(str) - 1
	while (str[j] <= str[i-1]):
		j = j - 1

	# Swap pivot with str[j]
	#str[i-1], str[j] = str[j], str[i-1]
	res = str[:i-1]+str[j]
	# reverse suffix
	tmp = str[i:j]+str[i-1]+str[(j+1):]
	res = res + tmp[::-1]

	return res





if __name__ == '__main__':
	str = raw_input().rstrip()
	print next_perm(str)

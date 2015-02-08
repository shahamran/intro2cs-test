def sort_radix(lst):
	# set a new list
	lst = lst[:]
	RADIX = 10
	max_length = False
	tmp, placement = -1, 1 # start from first digit (LSD)
	while not max_length:
		max_length = True
		# creates empty buckets
		buckets = [list() for _ in range(RADIX)]
		for i in lst:
			tmp = i // placement
			buckets[tmp % RADIX].append(i)
			# stops when the current digit is 0 for all nums in lst
			if max_length and tmp > 0:
				max_length = False
		a = 0
		for b in range(RADIX):
			buck = buckets[b]
			for i in buck:
				lst[a] = i
				a += 1
		placement *= RADIX
	return lst
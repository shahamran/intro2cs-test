def partial_sum(lst, num):
	if num < 0: return
	if len(lst) == 1:
		if lst[0] == num:
			return lst
		else:
			return
	for i in range(len(lst)):
		x = lst[i]
		if x == num: return [x]
		new_lst = lst[:i] + lst[i+1:]
		exists = partial_sum(new_lst, num - x)
		if exists: return exists + [x]
	return

""" Worst case runtime complexity: O(2 ** n)
    That's because in this case every sub-set of lst will be checked
    There are 2 ** n such sub-sets. """


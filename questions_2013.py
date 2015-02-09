# ex 1
def base_to_base(num, base1, base2):
	cnt = 0
	result = 0
	while num > 0:
		result += (num % base2) * (base1 ** cnt)
		num //= base2
		cnt += 1
	return result
	
# ex 7
def flatten(L):
	result = []
	for i in range(len(L)):
		item = L[i]
		if not type(item) is list:
			result.append(item)
		else:
			result += flatten(item)
	return result


# WordCombinations
class WordCombinations:
	def __init__(self, word_list):
		self.word_list = word_list
		self.curr_idx = 0
		self.all_words = 1
		for lst in word_list:
			lst.sort() # b
			self.all_words *= len(lst)

	def __iter__(self):
		return wc(self.word_list) # recursive
        return self # non-recursive

    #recursive
    def wc(word_list):
        if len(word_list) == 0: yield ''
        word_list[0].sort() # b
        SEP , END = ' ' , '.'
        for word in word_list[0]:
            if len(word_list) == 1:
                yield word + END
            else:
                for other in WordCombinations(word_list[1:]):
                    yield word + SEP + other

    # NON RECURSIVE
	def __next__(self):
		if self.curr_idx >= self.all_words: raise StopIteration
		N = len(self.word_list)
		SEP = ' '
		END = '.'
		sentence = ''
		for i in range(N):
			lst = self.word_list[i]
			others = 1
			for j in range(N - 1, i, -1):
				others *= len(self.word_list[j])
			idx = self.curr_idx // (others) % len(lst)
			sentence += self.word_list[i][idx]
			sentence += SEP if i < N - 1 else END
		self.curr_idx += 1
		return sentence

# print_reverse()
def read():
	return int(input())

def print_reverse():

	def helper(last = None):
		x = read()
		# print(x) (iv)
		if not last or x >= last:
			helper(x)
		print(x) # <-- delete (iv)

	helper()

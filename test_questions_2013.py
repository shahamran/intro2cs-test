from questions_2013 import *

def test_wc():
	word_list = [['I','You','We'],['love','hate'],['loving','hating','studying']]
	#wc = WordCombinations(word_list)
	for sentence in WordCombinations(word_list):
		print(sentence)
def test_reverse():
	print_reverse()

def test_bases():
	def legal(num, base1, base2):
		numbers = num.isnumeric() and \
				  base1.isnumeric() and \
				  base2.isnumeric()
		if not numbers: return
		num = int(num)
		base1 = int(base1)
		base2 = int(base2)
		base1_legal = base1 <= 10 and base1 >= 2
		base2_legal = base2 <= 10 and base2 >= 2
		if base1_legal and base2_legal:
			return num,base1,base2

	while True:
		num = input("Enter a number to be converted: ")
		base1 = input("From base: ")
		base2 = input("To base: ")
		is_legal = legal(num,base1,base2)
		if not is_legal:
			print('Illegal input. Try again.')
		else:
			num = is_legal[0]
			base1 = is_legal[1]
			base2 = is_legal[2]
			break

	result = base_to_base(num,base1,base2)
	print(str(num) + " in base " + str(base1) + " is "\
	    + str(result) + " in base " + str(base2))

def test_flatten(lst):
	print(flatten(lst))
	

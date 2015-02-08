from life_game import *
from random import randint

def generate_table(start = 7, end = 15):
	rnd = randint(start,end)
	table = []
	row = []
	for i in range(rnd):
		for j in range(rnd):
			row.append(True if randint(0,1) else False)
		table.append(row)
		row = []
	return table

ONE = '*'
ZERO = '-'
SEP = ' '
table = generate_table()
life = UltimateLife(table)
inpt = ''
for table in life:
	inpt = input()
	if inpt == 'end': break
	for x in range(len(table)):
		for y in range(len(table)):
			print(ONE if table[x][y] else ZERO, end = SEP)
		print('')
def alive(table, place):
	living_nbrs = 0
	N = len(table)
	NBRS = 3
	X, Y = place[0], place[1]
	END_VAL = [2,3] if table[X][Y] else [3]
	for x in range(NBRS):
		for y in range(NBRS):
			if (x,y) == place: continue
			i = (X + x - NBRS + 2) % N
			j = (Y + y - NBRS + 2) % N
			if table[i][j]: living_nbrs += 1
	for end_val in END_VAL:
		if living_nbrs == end_val: return True
	return False

def is_diff(table1,table2):
	N = len(table1)
	for x in range(N):
		for y in range(N):
			if table1[x][y] != table2[x][y]:
				return True
	return False

def Life(table):
	while True:
		new_table = [row[:] for row in table]
		N = len(table)
		for x in range(N):
			for y in range(N):
				new_table[x][y] = alive(table, (x,y))
		yield new_table
		table = new_table

def LifeC(table, prev_table = None):
	should_stop = False
	N = len(table)
	life = Life(table)
	while not should_stop:
		prev_table = [row[:] for row in table]
		table = next(life)
		if is_diff(table, prev_table):
			yield table
		else:
			should_stop = True

def LifeD(table):
	should_stop = False
	first = [row[:] for row in table]
	N = len(table)
	life = Life(table)
	while not should_stop:
		table = next(life)
		if is_diff(first, table):
			yield table
		else:
			should_stop = True

def UltimateLife(table):
	life = Life(table)
	lives = [table]
	should_stop = False
	while not should_stop:
		yield table
		lives.append(table)
		table = next(life)
		for a_life in lives:
			if not is_diff(a_life, table):
				should_stop = True
				break
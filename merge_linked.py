class Node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

def merge(x,y):
	if not x.next: return y
	if not y: return x
	if x.data <= y.data:
		new_y = x.next
		x.next = merge(y,new_y)
		return x
	else:
		new_x = y.next
		y.next = merge(x, new_x)
		return y
# -*- coding: utf-8 -*-
def yh(n):
	baseList = [1];
	for i in range(n):		
		print(baseList)
		baseList = [1] + [baseList[x] + baseList[x-1] for x in range(1,len(baseList))] + [1]
	return baseList
print(yh(5))



def Y_g():
	baseList = [1];
	while True:
		yield baseList
		baseList = [1] + [baseList[x] + baseList[x-1] for x in range(1,len(baseList))] + [1]
	

def Ytriangle_g():
	n = 0
	for t in Y_g():
		print(t)
		n = n + 1
		if n == 10:
			break
Ytriangle_g()

print([1] + [] + [1])
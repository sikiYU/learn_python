# -*- coding:utf-8 -*-
def Ytriangle(n):
	initList = [1]
	print(initList)
	for n in range(1,n):
		initList = [1] + [initList[x] + initList[x+1] for x in range(len(initList)-1)] + [1]
		print(initList)
Ytriangle(10)


def Ytriangle_g(n):
	initList = [1]
	while True:
		yield initList
		initList = [1] + [initList[x] + initList[x+1] for x in range(len(initList)-1)] + [1]

def Y_g():
	n = 0
	for t in Ytriangle_g(n):
		print(t)
		n = n + 1
		if n == 10:
			break
Y_g()

#试一试网上说的zip
def Ztriangle(n):
	initList = [1]
	print(initList)
	for n in range(1,n):
		initList = [x+y for x,y in zip(initList + [0], [0] + initList)]
		print(initList)
Ztriangle(10)

Z = zip([1,2,3,4,5],[5,4,3,2,1])
for x,y in Z:
	print(x,y)
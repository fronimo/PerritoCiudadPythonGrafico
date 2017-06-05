#import pygame,sys,Tkinter,random
#from pygame.locals import *

import random
import stddraw as d
import color as c

matrix=[]

def create_matrix(dim,matrix):
	fil = 0
	col = 0
	while fil < dim:
		list1=[]
		while col < dim:
			list1.append(0)
			col += 1
		matrix.append(list1)
		list1=[]
		col = 0
		fil += 1

def print_matrix(matrix):
	for fila in matrix:
		print fila



# 1 = abajo
# 2 = arriba
# 3 = izquierda
# 4 = derecha
listX = []
listY = []

def run_dog(times, dim, matrix, listX, listY):
	dimN = 100
	jump = (dimN/dim) #33.33
	radius = jump/2 #16

	posX = dim/2
	posY = dim/2
	listX.append(posX*10+jump+radius)
	listY.append(posY*10+jump+radius)
	matrix[posX][posY] = 1
	while posX != 0 and posX != dim-1 and posY != 0 and posY < dim-1:
		aleato = random.randint(1, 4)
		if aleato == 1:
			posX = posX+1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print 'abajo'
				print posX
				print posY
				listX.append(listX[-1]+jump)
				listY.append(listY[-1])
				print_matrix(matrix)
			else :
				print 'The dog is dead'
				return

		if aleato == 2:
			posX = posX-1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print 'arriba'
				print posX
				print posY
				listX.append(listX[-1]-jump)
				listY.append(listY[-1])
				print_matrix(matrix)
			else :
				print 'The dog is dead'
				return

		if aleato == 3:
			posY=posY-1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print_matrix(matrix)
				print 'izquierda'
				print posX
				print posY
				listX.append(listX[-1])
				listY.append(listY[-1]-jump)
				print_matrix(matrix)
			else:
				print 'The dog is dead'
				return

		if aleato == 4:
			posY=posY+1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print 'derecha'
				print posX
				print posY
				listX.append(listX[-1])
				listY.append(listY[-1]+jump)
				print_matrix(matrix)
			else:
				print 'The dog id dead'
				return
	print 'The dog is alive!'
	return


dimN = 100
dim = 6

d.setXscale(0, dimN+20)
d.setYscale(0, dimN+20)

place = 50

d.square((dimN/2)+10, (dimN/2)+10, dimN-((dimN/2)+10))
#d.filledSquare(50, place, 2)

# while place < 94:
# 	place+=1
# 	d.filledSquare(50, place ,2)
create_matrix(dim,matrix)
run_dog(2,dim,matrix,listX, listY)

d.line(20, 20, dimN, dimN)

x = [1, 2, 3]
y = [2, 4, 6]

tam = len(listX)
ini = 0
while ini < tam:
	d.filledSquare(listX[ini],listY[ini],(dimN/dim)/2)
	# d.setPenColor(c.BLACK)
	# d.text(50, 90, '1')
	ini += 1


print listX
print listY
#d.polygon(listX,listY)
#d.clear()


d.show(0)


c = ''
while c != '.':
	c = input()


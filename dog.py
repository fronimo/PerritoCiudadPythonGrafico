import random
# import stddraw as d
# import color as c

matrix=[]

try:
    dim=int(input('Dimension:'))
    times=int(input('Nro Intentos:'))
except ValueError:
    print ("Not a number")

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
		print (fila)

listX = []
listY = []

def run_dog(times, dim, matrix, listX, listY):
	_dim = float(dim)
	dimN = _dim*10
	jump =  _dim*10/2#33.33
	radius = jump/2 #16
	posX = int(dim/2)
	posY = int(dim/2)
	print('posX')
	print (posX)
	print('posY')
	print (posY)
	listX.append(jump)
	listY.append(jump)
	matrix[posX][posY] = 1
	while posX != 0 and posX != dim-1 and posY != 0 and posY < dim-1:
		aleato = random.randint(1, 4)
		if aleato == 1:
			posX = posX+1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print ('abajo')
				print (posX)
				print (posY)
				listX.append(listX[-1])
				listY.append(listY[-1]-10)
				print_matrix(matrix)
			else :
				print ('The dog is dead')
				return 0

		if aleato == 2:
			posX = posX-1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print ('arriba')
				print (posX)
				print (posY)
				listX.append(listX[-1])
				listY.append(listY[-1]+10)
				print_matrix(matrix)
			else :
				print ('The dog is dead')
				return 0

		if aleato == 3:
			posY=posY-1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print_matrix(matrix)
				print ('izquierda')
				print (posX)
				print (posY)
				listX.append(listX[-1]-10)
				listY.append(listY[-1])
				print_matrix(matrix)
			else:
				print ('The dog is dead')
				return 0

		if aleato == 4:
			posY=posY+1
			if matrix[posX][posY] == 0:
				matrix[posX][posY] = 1
				print ('derecha')
				print (posX)
				print (posY)
				listX.append(listX[-1]+10)
				listY.append(listY[-1])
				print_matrix(matrix)
			else:
				print ('The dog id dead')
				return 0
	print ('The dog is alive!')
	return 1


# dimN = dim*10
# centro = dimN/2
create_matrix(dim,matrix)
run_dog(times,dim,matrix,listX, listY)


# d.setXscale(0, dimN)
# d.setYscale(0, dimN)

# dimN = dim*10
# centro = dimN/2
# d.setXscale(0, dimN)
# d.setYscale(0, dimN)

# while times != 0:
# 	i = input("1 para seguir otro numero para cancelar: ")
# 	if i == 1:
		
# 		d.clear()
		
# 		create_matrix(dim,matrix)
# 		stil = run_dog(times,dim,matrix,listX, listY)
# 		tam = len(listX)
# 		ini = 0
# 		while ini < tam:
# 			d.square(listX[ini],listY[ini],5)
# 			d.setPenColor(d.BLUE)	
# 			d.text(listX[ini],listY[ini], str(ini))
# 			ini += 1

# 		if stil == 1:
# 			d.setPenColor(d.RED)	
# 			d.text(centro,3, "PERRITO VIVE! :D")
# 		else:
# 			d.setPenColor(d.RED)	
# 			d.text(centro,3, "PERRITO MUERE T.T")
# 		times-=1
# 		matrix = []
# 		listX = []
# 		listY = []
# 		d.show(0)
# 	else:
# 		break





# c = ''
# while c != '.':
# 	c = input()

import os

def tree(directorio,od=0):

	if os.path.exists(directorio):

		if od == 0:
			print(directorio)
			od = directorio.count('/',0)

		for parameter in os.listdir(directorio):
			path = directorio+'/'+parameter
			depth = path.count('/',0)
			print('|'*(depth-od)+'-'+parameter)
			if os.path.isdir(directorio+'/'+parameter):
				tree(directorio+'/'+parameter,od)

	else:

		print("El directorio no se encontro")			
		
    



    		
    
class Persona:
	def __init__(self, nombre, edad):
		self.__nombre=nombre
		self.__edad=edad

	def setNombre(self, n):
		self.__nombre=n

	def getNombre(self):
		return self.__nombre


	def setEdad(self, e):
		self.__edad=e

	def getEdad(self):
		return self.__edad


	nombre= property(setNombre,getNombre)
	edad= property(setEdad,getEdad)
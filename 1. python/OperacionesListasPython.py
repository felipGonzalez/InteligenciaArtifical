#Unir listas
my_lista = [1]

my_lista2 = [2,3,4]

my_lista3 = my_lista + my_lista2

my_lista3 # [1,2,3,4]

#Multiplicar elementos
my_lista = ['a']
my_lista2 = my_lista * 5
my_lista2 # ['a','a','a','a','a']
#Dividir listas
my_lista = [1,2,3,4,5]
my_lista_reversed = my_lista[::-1]
my_lista_reversed # [5,4,3,2,1]
#Eliminar ultimo elemento de la lista
my_lista = [1,2,3,4,5]
my_lista = my_lista.pop()
my_lista # [1,2,3,4]
#Ordenar lista
my_lista = [2,1,5,4,3]
my_lista = my_lista.sort()
my_lista # [1,2,3,4,5]
#Eliminar elemento
my_lista = [1,2,3,4,5]
del my_lista[0]
my_lista # [2,3,4,5]

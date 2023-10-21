### Tuplas ###
my_tuple = tuple()  # genera una tupla vacía
my_other_tuple = ()  # es análogo
# es un conjunto de valores
my_tuple = (27, 1.82, "Brian", "Parra")
print(my_tuple)
print(my_tuple[-1])
print(my_tuple.count(27))
print(my_tuple.index(27))
# aparenta ser lo mismo que una lista. Pero tiene menos operaciones
# my_tuple[1] = 1.85 son embargo, es inamovible, no puede modificarse
# print(my_tuple) esto por lo tanto mostrará error
# dicho de otra manera, es inmutable
my_other_tuple = (1.56,1.78,1.91)
my_sum_tuple = my_tuple+my_other_tuple
print(my_sum_tuple) #si se pueden concatenar
my_sum_tuple = list(my_sum_tuple) #siempre se puede cambiar de tipo
my_sum_tuple.append("José")
my_sum_tuple = tuple(my_sum_tuple) #y volver a tupla
print(my_sum_tuple)
del my_sum_tuple #también se puede borrar, pero completa
# print(my_sum_tuple) esto mostrará un error al no existir
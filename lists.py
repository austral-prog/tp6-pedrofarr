def remove_elements(lista):
    result = lista.copy()
    for index in [5, 4, 0]:
        if len(result) > index:
            result.pop(index)
    return result
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

def add_elements(lista):
    result = lista.copy()
    result.insert(0, 'Pink')
    result.append('Yellow')
    return result
print(add_elements(['Red', 'Green', 'White', 'Black']))

def is_empty(lista):
    return len(lista) == 0
print(is_empty([]))      
print(is_empty([1, 2]))   

def check_lists(lista1, lista2):
    if len(lista1) > 2 and len(lista2) > 2:
        return lista1[2] == lista2[2]
    return False
print(check_lists(['Black', 'Pink', 'Yellow', 'Red'], ['Red', 'Green', 'Yellow', 'White']))

def list_of_lists(lista_de_listas):
    result = []
    primera = lista_de_listas[0][:2]
    segunda = lista_de_listas[1][1:4]
    tercera = lista_de_listas[2][-2:]
    result.append(primera)
    result.append(segunda)
    result.append(tercera)
    return result
print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))
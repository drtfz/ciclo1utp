#usando map sin lambda
def doblar(numero):
    return numero*2

numero = [2,3,5,20,50]
print("usando map sin lambda")
print(list(map(doblar,numero))) #map hace una iteracion como la que hace el for


#usando map con lambda
numero = [2,3,5,20,50]
print("usando map con lambda")
print(list(map(lambda x: x*2, numero)))


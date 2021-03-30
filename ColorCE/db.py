
#Función para leer un archivo txt y obtener el max score
def get_score(route):
    file = open(route, 'r')
    temp_score = file.readline().split(':')[1]
    file.close()
    return int(temp_score)

# Función para sobreescribir el score del usuario
def update_score(route, new_score):
    file = open(route, 'w')
    file.write('TopScore:' + str(new_score))
    file.close()
update_score('user_score.txt', 0)
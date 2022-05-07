from pprint import pprint
import csv
import matplotlib.pyplot as plt



def leer_equipo(nombre_archivo):
    ''' 
    ----------
    Returns: lista de todo el equipo + potencial promedio de cada uno
    -------
    '''
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    #print(headers)
    
    players = []
    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        players.append(record)
        
    player_prom = []
        
    for p in players:    
        pot_max = float(p["pot_max"])
        pot_min = float(p["pot_min"])
        calculo = pot_max - ((pot_max - pot_min)/2)
        p["pot_prom"] = int(calculo)
        player_prom.append(p)
        
    return player_prom



def player_info(lista, nombre):
    player = []
    for l in lista:
        if l["nombre"] == nombre:
            player.append(l)
    return player



def national_player(lista, pais):
    national_team = []
    for l in lista:
        if l["pais"] == pais:
            national_team.append(l)
    return national_team



def pot_prom_nacional_individual(lista, pais):
    nat = national_player(lista, pais)
    proms = []
    dicc_proms_pais = {}
    dicc_proms_pais[pais] = proms
    for n in nat:
        pot = n["pot_prom"]
        name = n["apellido"]
        pot_name = pot, name
        proms.append(pot_name)
    return dicc_proms_pais



def tabla_potenciales(lista):
    print("\n")
    for l in lista:
        print("-" *40)
        print(f'Apellido: {l["apellido"]}' )
        print(f'Potencial: {l["pot_min"]}-{l["pot_max"]}' )
        print(f'Pot esperado: {l["pot_prom"]}' )
    print("-" *40)



def nacionalidades(lista):
    d_nacionalidades = {}
    paises = []
    # n = 0
    
    for l in lista:
        pais = l["pais"]
        paises.append(pais)
     
    set_paises = set(paises)
    
    for pais in set_paises:
        cantidad_por_pais = paises.count(pais)
        d_nacionalidades[pais] = cantidad_por_pais
    return d_nacionalidades



def plot_pie_naciones(diccionario):
    dicc = diccionario.items()
    paises = []
    cantidad = []
    for d in dicc:
        pais = d[0]
        n = d[1]
        paises.append(pais)
        cantidad.append(n)

    plt.axis("equal")
    plt.pie(cantidad ,labels = paises,autopct="%1.0f%%",startangle = 10)  
    plt.show()



def posiciones(lista):
    d_pos = {}
    posiciones = []
    
    for l in lista:
        pos = l["posicion"]
        posiciones.append(pos)
     
    set_posiciones = set(posiciones)
    
    for pos in set_posiciones:
        cantidad_por_pos = posiciones.count(pos)
        d_pos[pos] = cantidad_por_pos
    return d_pos    



def plot_pie_posiciones(diccionario):
    dicc = diccionario.items()
    posiciones = []
    cantidad = []
    for d in dicc:
        pos = d[0]
        n = d[1]
        posiciones.append(pos)
        cantidad.append(n)

    plt.axis("equal")
    plt.pie(cantidad ,labels = posiciones,autopct="%1.0f%%",startangle = 0)  
    plt.show()
    





'''
crear funcion future_stars() que genere una lista con los top 3 jugadores
con mejor potencial de toda la cantera. 
Para esto mi idea era ir haciendo 3 listas que cada una tenga al top 1,2, y 3
respectivamente, y despues se sumen esos 3 a una lista grande, no se me ocurre
otra opcion para ordenar los diccionarios adentro de la lista dependiendo del
potencial
'''



####################################################### 



team = leer_equipo("feyenoord.csv")
players = team
# pprint(team)


# player = player_info(team, "Josep")
# pprint(player)


# pais = national_player(players, "Argentina")
# print("La cantidad de jugadores de este pais en el equipo es:",len(pais))
# print("\n")
# pprint(pais)


# promedio_nacional_ind = pot_prom_nacional_individual(team, "Francia")
# print(promedio_nacional_ind)


# tabla = tabla_potenciales(team)


nations = nacionalidades(team)
print(nations)
plot_pie_naciones(nations)


posiciones = posiciones(team)
plot_pie_posiciones(posiciones)




















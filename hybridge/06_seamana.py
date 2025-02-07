import time

print("\nTe despiertas en un bosque oscuro. No recuerdas cómo llegaste aquí.")
time.sleep(2)
mochila = {"linterna": False, "cuchillo": False, "llave": False}

print("\nCerca de ti, ves una mochila con algunos objetos dentro.")
print("\nPuedes llevar un objeto contigo:")
print("1. Linterna")
print("2. Cuchillo")
print("3. Llave misteriosa")

eleccion = input("¿Cuál eliges? (1/2/3): ")

if eleccion == "1":
    mochila["linterna"] = True
    print("\nTomas la linterna. Ahora puedes ver mejor en la oscuridad.")
elif eleccion == "2":
    mochila["cuchillo"] = True
    print("\nTomas el cuchillo. Te sientes más seguro.")
elif eleccion == "3":
    mochila["llave"] = True
    print("\nTomas la llave misteriosa. ¿Para qué servirá?")
else:
    print("\nNo elegiste bien, así que sigues sin nada.")

print("\nCaminas por el bosque hasta que llegas a una cabaña abandonada.")
time.sleep(2)

if mochila["linterna"]:
    print("\nUsas la linterna para iluminar y ves que hay marcas extrañas en las paredes...")

print("\nLa puerta está cerrada. Intentas abrirla.")

if mochila["llave"]:
    print("\nUsas la llave y la puerta se abre. Entras con cautela...")
    print("\nDentro de la cabaña, hay un sonido proveniente del sótano.")
    time.sleep(2)
    decision = input("¿Bajas al sótano? (s/n): ")
    
    if decision.lower() == "s":
        if mochila["cuchillo"]:
            print("\nTe encuentras con una criatura horrible, pero logras defenderte con el cuchillo y escapas.")
            print("\nHas logrado escapar del bosque con vida. ¡Sobreviviste!")
        else:
            print("\nAlgo te ataca desde la oscuridad... No tienes cómo defenderte.")
            print("\nSientes un escalofrío en la espalda y, antes de reaccionar, todo se vuelve negro...")
            print("\nNo lograste sobrevivir.")
    else:
        print("\nDecides no bajar. Encuentras una ventana y logras escapar antes de que algo te atrape.")
        print("\nLogras salir de la cabaña y correr por el bosque, pero nunca sabrás qué había en el sótano.")
else:
    print("\nLa puerta no se abre y escuchas ruidos detrás de ti. Algo se acerca...")
    print("\nSientes un escalofrío en la espalda y, antes de reaccionar, todo se vuelve negro...")
    print("\nNo lograste sobrevivir.")
continuar = ""
tareas = {
    1: "Verificar los Niveles de Combustible",
    2: "Verificar el Sistema de Navegación",
    3: "Verificar los Sistemas de Soporte de Vida",
}

while continuar != "n":
    print("Tareas")
    for key, value in tareas.items():
        print(f"{key} - {value}")

    try:
        respuesta = int(input("Selecciona la tarea realizada: "))
        if respuesta in tareas:
            tarea_completada = tareas.pop(respuesta)
            print(f"Tarea {respuesta} completada y eliminada: {tarea_completada}")
        else:
            print("Opción no valida, intenta nuevamente...")
        
        if not tareas:
            print("Todas las tareas han sido completadas")
            break

        continuar = input("¿Deseas continuar s/n?: ").strip().lower()
        if continuar == "n" and tareas:
            print("Aun quedaron tareas por hacer")
        elif continuar == "n":
            print("Saliendo del programa")
            break
    except ValueError:
        print("Respuesta incorrecta, volver a intentar")
print("Tareas finalizadas")
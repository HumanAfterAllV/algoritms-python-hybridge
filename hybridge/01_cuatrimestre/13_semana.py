def explorar_territorio(tool_1, tool_2):
    tool_1_last_char = tool_1[-1].lower()
    tool_2_last_char = tool_2[-1].lower()

    if tool_1_last_char == "s" or len(tool_1) >= 5:
        print(f"Presiento que te irá mejor con esta herramienta: {tool_1}")
    elif tool_2_last_char == "s" or len(tool_2) >= 5:
        print(f"Presiento que te irá mejor con esta herramienta: {tool_2}")
    else:
        print("Las 2 herramientas son buenas opciones")

explorar_territorio("Cantimplora", "Brujulas")
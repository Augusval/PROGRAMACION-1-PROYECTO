import os
def equipos():
    print("==================================")
    print("=           EQUIPOS              =")
    print("==================================")
    n = ("---> Valentini Augusto\n --->Jesus Quijada\n --->Centurion G0nzalo\n --->Leomagno Ernesto\n --->Oksana Bernkhart\n --->Luis Agustin Chen")
    print("Equipos conformados por: \n" ,n)
    input("Enter para continuar...")
def juegoinfo():
    print("\n'El trivia'\n Es un juego interactivo de preguntas y respuestas que ofrece a los jugadores una experiencia desafiante y educativa.\n Gracias a una amplia gama de temas y niveles de dificultad, diseñadas para jugadores de todas las edades. \n Este juego combina elementos de competencia y aprendizaje, permitiendo a los usuarios probar y ampliar sus conocimientos en diversas áreas")
    print(" ")
    input("Enter para continuar...")
def trivias():
    os.system("cls")
    print("====================================================")
    print("=        ¡Bienvenido al menu de las trivias!       =")
    print("====================================================")
    print("->      1. Trivia Formula 1                      .<-")
    print("->      2. Trivia Cine                           .<-")
    print("->      3. Trivia Futbol                         .<-")
    print("->      4. Trivia Deporte General                .<-")
    print("->      5. Trivia Video Juegos                   .<-")
    print("->      6. Trivia Autos                          .<-")
    print("====================================================")
    print("=                    JUEGO                         =")
    print("====================================================")
    trivia = int(input("Ingrese opcion de trivia o enter para volver al menu: "))
    
    if trivia == 1:
        print()
        print("======[Bienvenido trivia del Formula 1]======")
        print()
        from preguntas import Formula
        print("""
        $$$$$$$$\  $$$$$$\  $$$$$$$\  $$\      $$\ $$\   $$\ $$\       $$$$$$\        $$\   $$\ $$\   $$\  $$$$$$\  
        $$  _____|$$  __$$\ $$  __$$\ $$$\    $$$ |$$ |  $$ |$$ |     $$  __$$\       $$ |  $$ |$$$\  $$ |$$  __$$\ 
        $$ |      $$ /  $$ |$$ |  $$ |$$$$\  $$$$ |$$ |  $$ |$$ |     $$ /  $$ |      $$ |  $$ |$$$$\ $$ |$$ /  $$ |
        $$$$$\    $$ |  $$ |$$$$$$$  |$$\$$\$$ $$ |$$ |  $$ |$$ |     $$$$$$$$ |      $$ |  $$ |$$ $$\$$ |$$ |  $$ |
        $$  __|   $$ |  $$ |$$  __$$< $$ \$$$  $$ |$$ |  $$ |$$ |     $$  __$$ |      $$ |  $$ |$$ \$$$$ |$$ |  $$ |
        $$ |      $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |     $$ |  $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |
        $$ |       $$$$$$  |$$ |  $$ |$$ | \_/ $$ |\$$$$$$  |$$$$$$$$\$$ |  $$ |      \$$$$$$  |$$ | \$$ | $$$$$$  |
        \__|       \______/ \__|  \__|\__|     \__| \______/ \________\__|  \__|       \______/ \__|  \__| \______/ 
                                                                                                            
        """)
        Formula()
        input("Enter Para Continuar...")
    elif trivia == 2:
        print()
        print("======[Bienvenido trivia del Cine]======")
        print()
        from preguntas import Cine
        print("""
          /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$
         /$$__  $$|_  $$_/| $$$ | $$| $$_____/
        | $$  \__/  | $$  | $$$$| $$| $$      
        | $$        | $$  | $$ $$ $$| $$$$$   
        | $$        | $$  | $$  $$$$| $$__/   
        | $$    $$  | $$  | $$\  $$$| $$      
        |  $$$$$$/ /$$$$$$| $$ \  $$| $$$$$$$$
        \______/ |______/|__/  \__/|________/
                           
        """)
        Cine()
        input("Enter Para Continuar...")

    elif trivia == 3:
        print()
        print("======[Bienvenido trivia del Futbol]======")
        print()
        from preguntas import Futbol
        print("""
         /$$$$$$$$          /$$     /$$                 /$$
        | $$_____/         | $$    | $$                | $$
        | $$    /$$   /$$ /$$$$$$  | $$$$$$$   /$$$$$$ | $$
        | $$$$$| $$  | $$|_  $$_/  | $$__  $$ /$$__  $$| $$
        | $$__/| $$  | $$  | $$    | $$  \ $$| $$  \ $$| $$
        | $$   | $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$
        | $$   |  $$$$$$/  |  $$$$/| $$$$$$$/|  $$$$$$/| $$
        |__/    \______/    \___/  |_______/  \______/ |__/
                                                                                
        """)
        Futbol()
        input("Enter Para Continuar...")

    elif trivia == 4:
        print()
        print("======[Bienvenido trivia del Deporte General]======")
        print()
        from preguntas import DeporteGral
        print("""
         /$$$$$$$                                            /$$                      /$$$$$$                                                   /$$
        | $$__  $$                                          | $$                     /$$__  $$                                                 | $$
        | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ | $$
        | $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$      | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$| $$
        | $$  | $$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/  | $$    | $$$$$$$$      | $$|_  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/ /$$$$$$$| $$
        | $$  | $$| $$_____/| $$  | $$| $$  | $$| $$        | $$ /$$| $$_____/      | $$  \ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$| $$
        | $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$/| $$        |  $$$$/|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$| $$
        |_______/  \_______/| $$____/  \______/ |__/         \___/   \_______/       \______/  \_______/|__/  |__/ \_______/|__/      \_______/|__/
                            | $$                                                                                                                   
                            | $$                                                                                                                   
                            |__/                                                                                                                   
        """)
        DeporteGral()
        input("Enter Para Continuar...")

    elif trivia == 5:
        print()
        print("======[Bienvenido trivia del Video Juegos]======")
        print()
        from preguntas import VideoJuegos
        print("""
         /$$    /$$ /$$       /$$                              /$$$$$                                                  
        | $$   | $$|__/      | $$                             |__  $$                                                  
        | $$   | $$ /$$  /$$$$$$$  /$$$$$$   /$$$$$$             | $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$
        |  $$ / $$/| $$ /$$__  $$ /$$__  $$ /$$__  $$            | $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/
        \  $$ $$/ | $$| $$  | $$| $$$$$$$$| $$  \ $$       /$$  | $$| $$  | $$| $$$$$$$$| $$  \ $$| $$  \ $$|  $$$$$$ 
         \  $$$/  | $$| $$  | $$| $$_____/| $$  | $$      | $$  | $$| $$  | $$| $$_____/| $$  | $$| $$  | $$ \____  $$
          \  $/   | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/      |  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/ /$$$$$$$/
           \_/    |__/ \_______/ \_______/ \______/        \______/  \______/  \_______/ \____  $$ \______/ |_______/ 
                                                                                           /$$  \ $$                    
                                                                                           |  $$$$$$/                    
                                                                                            \______/                      
        """)
        VideoJuegos()
        input("Enter Para Continuar...")

    elif  trivia == 6:
        print()
        print("======[Bienvenido trivia de Autos]======")
        print()
        from preguntas import Auto
        print(""")
          /$$$$$$              /$$                        
         /$$__  $$            | $$                        
        | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$$
        | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$ /$$_____/
        | $$__  $$| $$  | $$  | $$    | $$  \ $$|  $$$$$$ 
        | $$  | $$| $$  | $$  | $$ /$$| $$  | $$ \____  $$
        | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/ /$$$$$$$/
        |__/  |__/ \______/    \___/   \______/ |_______/ 
                                                  
        """)
        Auto()
        input("Enter Para Continuar...")
    else:
        return input("Enter para volver al menu...")
    
def menu():
    repetir = True
    while repetir:
        os.system("cls")
        print("============================================================================================")
        print("=                 ¡Bienvenido al menu elija alguna de las opciones!                        =")
        print("============================================================================================")
        print("------->          1.  Juego Trivia                                            .<------------")
        print("------->          2.  Crear preguntas                                         .<------------")
        print("------->          3.  Puntajes                                                .<------------")
        print("------->          4.  Instrucciones                                           .<------------")
        print("------->          5.  Equipo                                                  .<------------")
        print("------->          6.  Salir                                                   .<------------")
        print("============================================================================================")
        print("=                                          MENU                                            =")
        print("============================================================================================")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                modo()
            elif opcion == 2:
                crear_preguntas()
            elif opcion == 4:
                juegoinfo()
            elif opcion == 3:
                print("Funcion de puntajes.")
                input('Presione enter para continuar...')
            elif opcion == 5:
                equipos()
            elif opcion == 6:
                print("Cerrando...")
                repetir = False
        except:
                print("Formato ingresado no aceptado...")
                input("Enter para continuar...")
def modo():
    repetir = True
    while repetir:
        os.system("cls")
        print("============================================================================================")
        print("=                      ¡Seleccione el modo de juego!                                       =")
        print("============================================================================================")
        print("------->          1.  Un jugador                                              .<------------")
        print("------->          2.  Versus                                                  .<------------")
        print("------->          3.  Volver                                                  .<------------")
        print("============================================================================================")
        print("=                                          MENU                                            =")
        print("============================================================================================")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                selectdificultad()
            elif opcion == 2:
                #versus()
                pass
            elif opcion==3:
                menu()    
        except:
            print("Formato ingresado no aceptado...")
            input("Enter para continuar...")
def crear_preguntas():
    repetir = True
    while repetir:
        os.system("cls")
        print("============================================================================================")
        print("=                ¡Seleccione el tema para el que desea crear preguntas!                    =")
        print("============================================================================================")
        print("------->          1.  Seleccionar tema                                        .<------------")
        print("------->          2.  Volver                                                  .<------------")
        print("============================================================================================")
        print("=                                          MENU                                            =")
        print("============================================================================================")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                #crearpregunta()
                pass
            elif opcion == 2:
                menu()
        except:
            print("Formato ingresado no aceptado...")
            input("Enter para continuar...")

def selectdificultad():
    repetir = True
    while repetir:
        os.system("cls")
        print("============================================================================================")
        print("=                      ¡Seleccione la dificultad!                                          =")
        print("============================================================================================")
        print("------->          1.  Facil                                                   .<------------")
        print("------->          2.  Medio                                                   .<------------")
        print("------->          3.  Dificil                                                 .<------------")
        print("------->          4.  Volver                                                  .<------------")
        print("============================================================================================")
        print("=                                          MENU                                            =")
        print("============================================================================================")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                #variable dificultad facil
                trivias()
            elif opcion == 2:
                #variable dificultad medio
                trivias()
            elif opcion == 3:
                #variable dificultad dificl
                trivias()
            elif opcion == 4:
                menu()
        except:
            print("Formato ingresado no aceptado...")
            input("Enter para continuar...")


menu()


#if __name__ == "__main__":
#    main()




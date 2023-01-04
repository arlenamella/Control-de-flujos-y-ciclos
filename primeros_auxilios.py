estimulos = input("¿Responde a estímulos? Respoder con si o no: ").lower()
if estimulos == str("no"):
    print("Abrir la vía aérea")
    respira = input("¿Respira? Responde si o no: ")
    if respira == str("no"):
        print("Administrar 5 ventilaciones y llamar a Ambulancia")
        signosDeVida = input("¿Signos de Vida? Respode si o no: ")
        ambulancia = "no"
        while ambulancia != "si":
            if signosDeVida == str("no"):
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
                ambulancia = input("¿LLegó la ambulancia? Responde si o no: ")
            else:
                print("Reevaluar a la espera de la Ambulancia")
                ambulancia = input("¿LLegó la ambulancia? Responde si o no: ")
    else:
        print("Permitirle posición de suficiente Ventilación")
else:
   print("Valorar la necesidad de llevarlo al hospital más cercano")
        
       

    
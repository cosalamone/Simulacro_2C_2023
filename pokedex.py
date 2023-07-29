# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    ##### ! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    ##### ! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    ##### ! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Squirtle", "Psyduck", "Vaporeon", "Charizard", "Psyduck", "Vaporeon", "Squirtle", "Mewtwo", "Charizard", "Vaporeon"]
        self.lista_poder_pokemones = [90, 70, 150, 160, 70, 180, 100, 200, 170, 160]
        self.lista_tipo_pokemones = ["agua", "psíquico", "agua", "fuego", "psíquico", "agua", "agua", "psíquico", "fuego", "agua"]

    def btn_mostrar_todos_on_click(self):
        #B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal).

        for posicion in range(len(self.lista_tipo_pokemones)):

            nombre = self.lista_nombre_pokemones[posicion]

            print(f' {nombre} -- {posicion}\n')

        

    
    def btn_mostrar_informe_1(self):
    ##### ! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
        contador_total = 0 
        contador_psiquico = 0
        for i in range(len(self.lista_tipo_pokemones)):
            tipo = self.lista_tipo_pokemones[i]
            poder = self.lista_poder_pokemones[i]

            contador_total += 1
            if tipo == "psíquico" and poder <= 150:
                contador_psiquico += 1 

        porcentaje = contador_psiquico * 100 / contador_total


        print(f'El porcentaje de pokemons de tipo psiquico, con pelea inferior o igual a 150 es de : {porcentaje:.0f}%')


    def btn_mostrar_informe_2(self):
    ##### ! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).

        contador_total = 0
        contador_agua = 0  # > 100 poder, # % sobre el total 

        for i in range(len(self.lista_tipo_pokemones)):
            tipo = self.lista_tipo_pokemones[i]
            poder = self.lista_poder_pokemones[i]

            contador_total += 1
            if tipo == "agua" and poder > 100:
                contador_agua += 1 
        
        porcentaje = contador_agua * 100 / contador_total

        print(f'El porcentaje de pokemons de tipo agua, con poder de pelea > a 100 es de:{porcentaje:.0f}%')

    def btn_mostrar_informe_3(self):
    ##### ! 7) - tipo de los pokemones del tipo que menos pokemones posea. 

        contador_agua = 0
        contador_psiquico = 0
        contador_fuego = 0

        for i in range(len(self.lista_tipo_pokemones)):
            tipo = self.lista_tipo_pokemones[i]

            if tipo == "agua":
                contador_agua += 1
            else: 
                if tipo == 'psíquico':
                    contador_psiquico += 1
                else: 
                    if tipo == 'fuego':
                        contador_fuego += 1


        if contador_agua < contador_fuego and contador_agua < contador_psiquico:
            print(f'El tipo de pokemon que menos cantidad posee es: AGUA')
        else:
            if contador_psiquico < contador_fuego:
                print(f'El tipo de pokemnos que menos cantidad posee es: PSIQUICO')
            else: 
                print(f'El tipo de pokemno que menos cantidad posee es: FUEGO')


    
    def btn_cargar_pokedex_on_click(self):

        contador = 0
        while contador < 10:
            contador += 1

            nombre = prompt('utn', 'Ingrese el nombre del pokemon')
            while len(nombre) < 3:
                nombre = prompt('utn', 'Ingrese un nombre valido')
            self.lista_nombre_pokemones.append(nombre)

            tipo = prompt('utn', 'Ingrese el tipo del pokemon (Agua, Psiquico, Fuego)')
            while tipo != 'Agua' and tipo != 'Psiquico' and tipo != 'Fuego':
                tipo = prompt('utn', 'Verificar: los tipos de pokemon son: Agua, Psiquico, Fuego')
            self.lista_tipo_pokemones.append(tipo)

            poder = int(prompt('utn', 'Ingrese el Poder de ataque')) 
            while poder < 50 or poder > 200: 
                poder = int(prompt('utn', 'Verificar: el poder debe ser entre 50 y 200') )
            self.lista_poder_pokemones.append(poder)



            
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
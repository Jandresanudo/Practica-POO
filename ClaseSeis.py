class Medicamento:
    def __init__(self):
        self.__nombre = ""  # Encapsulamiento: atributo privado
        self.__dosis = 0    # Encapsulamiento: atributo privado

    # Getter para el nombre del medicamento
    def verNombre(self):
        return self.__nombre

    # Getter para la dosis del medicamento
    def verDosis(self):
        return self.__dosis

    # Setter para asignar el nombre del medicamento
    def asignarNombre(self, med):
        self.__nombre = med

    # Setter para asignar la dosis del medicamento
    def asignarDosis(self, med):
        self.__dosis = med


class Mascota:
    def __init__(self):
        self.__nombre = ""                  # Encapsulamiento: atributo privado
        self.__historia = 0                 # Encapsulamiento: atributo privado
        self.__tipo = ""                    # Encapsulamiento: atributo privado
        self.__peso = ""                    # Encapsulamiento: atributo privado
        self.__fecha_ingreso = ""           # Encapsulamiento: atributo privado
        self.__lista_medicamentos = []      # Encapsulamiento: atributo privado

    # Getter para el nombre de la mascota
    def verNombre(self):
        return self.__nombre

    # Getter para la historia clínica de la mascota
    def verHistoria(self):
        return self.__historia

    # Getter para el tipo de mascota
    def verTipo(self):
        return self.__tipo

    # Getter para el peso de la mascota
    def verPeso(self):
        return self.__peso

    # Getter para la fecha de ingreso de la mascota
    def verFecha(self):
        return self.__fecha_ingreso

    # Getter para la lista de medicamentos de la mascota
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos

    # Setter para asignar el nombre de la mascota
    def asignarNombre(self, n):
        self.__nombre = n

    # Setter para asignar la historia clínica de la mascota
    def asignarHistoria(self, nh):
        self.__historia = nh

    # Setter para asignar el tipo de mascota
    def asignarTipo(self, t):
        self.__tipo = t

    # Setter para asignar el peso de la mascota
    def asignarPeso(self, p):
        self.__peso = p

    # Setter para asignar la fecha de ingreso de la mascota
    def asignarFecha(self, f):
        self.__fecha_ingreso = f

    # Setter para asignar la lista de medicamentos de la mascota
    def asignarLista_Medicamentos(self, n):
        self.__lista_medicamentos = n


class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []  # Encapsulamiento: atributo privado

    # Método para verificar si una mascota ya existe en el sistema
    def verificarExiste(self, historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        return False

    # Método para obtener el número de mascotas en el sistema
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)

    # Método para ingresar una mascota al sistema
    def ingresarMascota(self, mascota):
        self.__lista_mascotas.append(mascota)

    # Método para obtener la fecha de ingreso de una mascota
    def verFechaIngreso(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha()
        return None

    # Método para obtener los medicamentos de una mascota
    def verMedicamento(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos()
        return None

    # Método para eliminar una mascota del sistema
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)
                return True
        return False


def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu = int(input('''\nIngrese una opción:
                       \n1- Ingresar una mascota
                       \n2- Ver fecha de ingreso
                       \n3- Ver número de mascotas en el servicio
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota
                       \n6- Salir
                       \nUsted ingresó la opción: '''))
        if menu == 1:  # Ingresar una mascota
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...")
                continue
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre = input("Ingrese el nombre de la mascota: ")
                tipo = input("Ingrese el tipo de mascota (felino o canino): ")
                peso = int(input("Ingrese el peso de la mascota: "))
                fecha = input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm = int(input("Ingrese cantidad de medicamentos: "))
                lista_med = []

                for i in range(0, nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis = int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el número de historia clínica")

        elif menu == 2:  # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 3:  # Ver número de mascotas en el servicio
            numero = servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu == 4:  # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q)
            if medicamento != None:
                print("Los medicamentos suministrados son: ")
                for m in medicamento:
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5:  # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q)
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con éxito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break

        else:
            print("Usted ingresó una opción no válida, inténtelo nuevamente...")

if __name__ == '__main__':
    main()

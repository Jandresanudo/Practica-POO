class Paciente:
    def __init__(self):
        # Constructor: Inicializa los atributos del paciente
        self.__nombre = ''      # Encapsulamiento: Los atributos están encapsulados
        self.__cedula = 0       # Getter y Setter: Proporcionan acceso controlado a los atributos
        self.__genero = ''      # Encapsulamiento
        self.__servicio = ''    # Encapsulamiento

    # Métodos get: Devuelven los valores de los atributos
    def verNombre(self):
        return self.__nombre

    def verCedula(self):
        return self.__cedula

    def verGenero(self):
        return self.__genero

    def verServicio(self):
        return self.__servicio

    # Métodos set: Establecen los valores de los atributos
    def asignarNombre(self, nombre):
        self.__nombre = nombre

    def asignarCedula(self, cedula):
        self.__cedula = cedula

    def asignarGenero(self, genero):
        self.__genero = genero

    def asignarServicio(self, servicio):
        self.__servicio = servicio

class Sistema:
    def __init__(self):
        # Constructor: Inicializa la lista de pacientes del sistema
        self.__lista_pacientes = []

    # Método para verificar la existencia de un paciente en el sistema
    def verificarPaciente(self, cedula):
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                return True
        return False

    # Método para agregar un paciente al sistema
    def ingresarPaciente(self, paciente):
        self.__lista_pacientes.append(paciente)
        return True

    # Método para ver los datos de un paciente por su cédula
    def verDatosPaciente(self, cedula):
        if self.verificarPaciente(cedula) == False:
            return None
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                return paciente

    # Método para ver el número de pacientes en el sistema
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")

def main():
    # Crear una instancia del sistema
    sistema = Sistema()

    while True:
        # Menú de opciones
        opcion = int(input("\nIngrese:\n0 para salir,\n1 para ingresar nuevo paciente,\n2 para ver paciente\n\t--> "))

        if opcion == 1:
            print("A continuación se solicitarán los datos ...")
            # Ingresar datos del nuevo paciente
            cedula = int(input("Ingrese la cédula: "))
            if sistema.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cédula >>".upper())
            else:
                paciente = Paciente()
                paciente.asignarNombre(input("Ingrese el nombre: "))
                paciente.asignarCedula(cedula)
                paciente.asignarGenero(input("Ingrese el género: "))
                paciente.asignarServicio(input("Ingrese el servicio: "))
                resultado = sistema.ingresarPaciente(paciente)
                if resultado:
                    print("Paciente ingresado")
                else:
                    print("No ingresado")
        elif opcion == 2:
            cedula = int(input("Ingrese la cédula a buscar: "))
            # Buscar y mostrar datos del paciente
            paciente = sistema.verDatosPaciente(cedula)
            if paciente != None:
                print("Nombre: " + paciente.verNombre())
                print("Cédula: " + str(paciente.verCedula()))
                print("Género: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
            else:
                print("No existe un paciente con esa cédula")
        elif opcion == 0:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
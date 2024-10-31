class Libro:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

  def mostrar_informacion(self):
    print(f"Título: {self.titulo}")
    print(f"Autor: {self.autor}")

class Usuario:
  def __init__(self, nombre):
    self.nombre = nombre

  def mostrar_informacion(self):
    print(f"Nombre: {self.nombre}")

class Prestamo:
  def __init__(self, libro, usuario, fecha_prestamo, fecha_devolución):
    self.libro = libro
    self.usuario = usuario
    self.fecha_prestamo = fecha_prestamo
    self.fecha_devolución = fecha_devolución

  def mostrar_informacion(self):
    print("Información del préstamo:")
    self.libro.mostrar_informacion()
    self.usuario.mostrar_informacion()

    def capturar_informaciom_libro():
  #captura el titulo y autor del libro
  titulo = input("Ingrese el título del libro: ")
  autor = input("Ingrese el autor del libro: ")
  return Libro(titulo, autor)

def capturar_informacion_usuario():
  #captura el nombre del usuario
  nombre = input("Ingrese su nombre: ")
  return Usuario(nombre)

#def realizar_prestamo(libro, usuario):
  #Realizar el prestamo del libro
  #return Prestamo(libro, usuario, "2023-08-01", "2023-08-15")

def realizar_prestamo():
  #Captura información del libro y del usuario y crea un objeto de prestamo
  libro = capturar_informaciom_libro()
  usuario = capturar_informacion_usuario()
  prestamo = Prestamo(libro, usuario, "2023-08-01", "2023-08-15")
  print(prestamo.mostrar_informacion())

#Ejecucuión
if __name__ == "__main__":
  realizar_prestamo()
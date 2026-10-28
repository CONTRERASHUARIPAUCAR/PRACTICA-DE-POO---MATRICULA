class Matricula:
  def __init__(self, full_name):
    self.__full_name = full_name

  @property
  def full_name(self):
    return self.__full_name

  @full_name.setter
  def full_name(self, full_name):
    self.__full_name = full_name

  def costo(self):
    return 60.00

  def information(self):
    print(f"Estudiante: {self.__full_name}")
    print(f"Monto a pagar: S/ {self.costo():.2f}")


class MatriculaExtemporanea(Matricula):
  def __init__(self, full_name):
    super().__init__(full_name)

  def costo(self):
    return super().costo() + 15.00


class MatriculaDesaprobatoria(Matricula):
  def __init__(self, full_name):
    super().__init__(full_name)

  def costo(self):
    return super().costo() + 15.00


class MatriculaBeca(Matricula):
  def __init__(self, full_name):
    super().__init__(full_name)

  def costo(self):
    return super().costo() / 2


# Programador 1
# Orden (MRO): Combinada1 -> Beca -> Desaprobatoria -> Extemporanea -> Matricula
class MatriculaCombinada1(MatriculaBeca, MatriculaDesaprobatoria, MatriculaExtemporanea):
  def __init__(self, full_name):
    Matricula.__init__(self, full_name)


# Programador 2
# Orden (MRO): Combinada2 -> Desaprobatoria -> Extemporanea -> Beca -> Matricula
class MatriculaCombinada2(MatriculaDesaprobatoria, MatriculaExtemporanea, MatriculaBeca):
  def __init__(self, full_name):
    Matricula.__init__(self, full_name)


# Si se pone la clase general primero, Python da error:
# class MatriculaError(Matricula, MatriculaBeca):
#   pass
# TypeError: Cannot create a consistent method resolution order (MRO)


# Rediseño: para cada estudiante se decide si la beca va antes o despues de los recargos
class MatriculaCorregida(Matricula):
  def __init__(self, full_name, extemporanea, desaprobatoria, beca, beca_primero):
    super().__init__(full_name)
    self.__extemporanea = extemporanea
    self.__desaprobatoria = desaprobatoria
    self.__beca = beca
    self.__beca_primero = beca_primero

  @property
  def extemporanea(self):
    return self.__extemporanea

  @property
  def desaprobatoria(self):
    return self.__desaprobatoria

  @property
  def beca(self):
    return self.__beca

  @property
  def beca_primero(self):
    return self.__beca_primero

  @extemporanea.setter
  def extemporanea(self, extemporanea):
    self.__extemporanea = extemporanea

  @desaprobatoria.setter
  def desaprobatoria(self, desaprobatoria):
    self.__desaprobatoria = desaprobatoria

  @beca.setter
  def beca(self, beca):
    self.__beca = beca

  @beca_primero.setter
  def beca_primero(self, beca_primero):
    self.__beca_primero = beca_primero

  def costo(self):
    monto = super().costo()
    if self.__beca and self.__beca_primero:
      monto = monto / 2
    if self.__extemporanea:
      monto = monto + 15.00
    if self.__desaprobatoria:
      monto = monto + 15.00
    if self.__beca and not self.__beca_primero:
      monto = monto / 2
    return monto

  def information(self):
    super().information()
    if self.__beca_primero:
      print("Beca aplicada: antes de los recargos")
    else:
      print("Beca aplicada: despues de los recargos")


print("==== Programador 1 ====")
object1 = MatriculaCombinada1("Luis Huamaní Cárdenas")
object1.information()

print("")
print("==== Programador 2 ====")
object2 = MatriculaCombinada2("Rosa Ccahuana Prado")
object2.information()

print("")
print("==== Rediseño ====")
object3 = MatriculaCorregida("Luis Huamaní Cárdenas", True, True, True, False)
object3.information()
print("")
object4 = MatriculaCorregida("Rosa Ccahuana Prado", True, True, True, False)
object4.information()

print("")
print("==== Cambiando el orden con el setter ====")
object4.beca_primero = True
object4.information()

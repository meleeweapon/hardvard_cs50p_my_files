import random
  
def main() -> None:
  # student_main()
  # types()
  # hat()
  # student_main_2()
  # wizard()
  vault()

class Student():
  def __init__(self, name, house) -> None:
    self.name = name
    self.house = house
  
  def __str__(self) -> str:
    return f"{self.name} from {self.house}"
  
  @property
  def house(self):
    return self._house
  
  @house.setter
  def house(self, house):
    if house not in ["gryffindor", "hogwarts"]:
      raise ValueError("unexpected place")
    self._house = house

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("missing name")
    self._name = name
  
def student_main():
  student = get_student()
  print(student)

def get_student():
  name = input("name: ")
  house = input("house: ")
  return Student(name, house)

def types():
  print(type(50))
  print(type("booba"))
  print(type([]))
  print(type({}))


class Hat:
  houses = ["gryffindor", "hogwarts"]

  @classmethod
  def sort(cls, name):
    place = random.choice(cls.houses)
    return f"{name} is in {place}"

def hat():
  print(
    Hat.sort("harry")
  )


class Student_2():
  def __init__(self, name, house) -> None:
    self.name = name
    self.house = house
  
  def __str__(self) -> str:
    return f"{self.name} from {self.house}"
  
  @property
  def house(self):
    return self._house
  
  @house.setter
  def house(self, house):
    if house not in ["gryffindor", "hogwarts"]:
      raise ValueError("unexpected place")
    self._house = house

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("missing name")
    self._name = name


  @classmethod
  def get_student(cls):
    name = input("name: ")
    house = input("house: ")
    return cls(name, house)


def student_main_2():
  print(Student_2.get_student())



class Wizard:
  def __init__(self, name) -> None:
    self.name = name
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("name is empty")
    self._name = name

class Student_3(Wizard):
  def __init__(self, name, house) -> None:
    super.__init__(name)
    self.house = house

class Proffesor(Wizard):
  def __init__(self, name, subject) -> None:
    super.__init__(name)
    self.subject = subject

def wizard():
  wizard = Wizard("albus")
  student = Student_3("harry", "gryffindor")
  proffesor = Proffesor("severus", "defense")


class Vault:
  def __init__(self, galleons=0, sickles=0, knuts=0) -> None:
    self.galleons = galleons
    self.sickles = sickles
    self.knuts = knuts
  
  def __str__(self) -> str:
    return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"
  
  def __add__(self, other):
    galleons = self.galleons + other.galleons
    sickles = self.sickles + other.sickles
    knuts = self.knuts + other.knuts

    return Vault(galleons, sickles, knuts)


def vault():
  potter = Vault(100, 50, 25)
  print(potter)

  weasley = Vault(25, 50, 100)
  print(weasley)

  total = potter + weasley
  print(total)

if __name__ == '__main__':
  main()
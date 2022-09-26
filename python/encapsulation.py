class Base:
    def __init__(self,age) -> None:
        self._name="B S Kaurav"
        self._age=age
        self.__newAge=67

class Derived(Base):
    def __init__(self) -> None:
        super().__init__(23)

        print(f"calling protected member of base class : {self._age}")

        self._age=24
        print(f"calling modified protected member outside class : {self._age}")

obj1=Base(44)
obj2=Derived()

print(f"Accessing private from obj1 : {obj1._name}")
print(f"Accessing private from obj1 : {obj1._age}")
print(f"Accessing private from obj1 : {obj1.__newAge}")

class bancoDeDados:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def getName(self):
        return self.name

    @property
    def getAge(self):
        return self.age

    def setName(self, name):
        return self.name

    def setAge(self, age):
        return self.age

    @property
    def aniversario(self):
        self.age += 1
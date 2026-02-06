class person:
    def __init__(self,name, age, sex, city):
        self.name = name
        self.age = age
        self.sex = sex
        self.city = city

    def Person_name(self):
        print(f"the person name is {self.name}")
    
    def Person_info(self):
        print(f"the person info are : {self.name} - {self.age} - {self.sex} - {self.city}")


person1 = person("anurag", 21, 'male', 'xyz')
person1.Person_name()
person1.Person_info()
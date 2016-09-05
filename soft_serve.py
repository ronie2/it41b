class Person:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        if type(self) == Person:
            return "'Person' object with '{name}' name".format(name=self.name)
        elif type(self) == Student:
            return "'Student' object with '{education}' education".format(
                education=self.education)
        elif type(self) == Worker:
            return "'Worker' object with '{work_place}' work place".format(
                work_place=self.work_place)

    @property
    def name(self):
        return self.__name

    def show_data(self):
        print(self.name)


class Student(Person):
    def __init__(self, person, education):
        self.__education = education
        if type(person) == Person:
            self.__person = person
        else:
            raise Exception("Expected type: 'Person'")

    # def __repr__(self):
    #     return "'Student' object with '{education}' education".format(
    #         education=self.education)

    @property
    def education(self):
        return self.__education

    @property
    def person(self):
        return self.__person


class Worker(Person):
    def __init__(self, person, work_place):
        self.__work_place = work_place
        if type(person) == Person:
            self.__person = person
        else:
            raise Exception(
                "Expected type: {ex_type} got: {actual_type}".format(
                    ex_type=Person,
                    actual_type=type(person)))

    # def __repr__(self):
    #     return "'Worker' object with '{work_place}' work place".format(
    #         work_place=self.work_place)

    @property
    def work_place(self):
        return self.__work_place


class Academy:
    def __init__(self):
        self.__collection = []

    @property
    def collection(self):
        return self.__collection

    def show_all(self):
        for man in self.collection:
            print(man)

    def add_person(self, man):
        if type(man) == Student or type(man) == Worker:
            self.collection.append(man)
        else:
            raise Exception("Expected type: 'Student' or 'Worker'")

    def __repr__(self):
        return "'Academy' object with '{count}' persons".format(
            count=len(self.collection))

    def __len__(self):
        return len(self.collection)


# Create and show Student
person1 = Person("Roman")
student = Student(person1, "Higher")
print(student)
print("*" * 50)

# Create and show Worker
person2 = Person("Igor")
worker = Worker(person2, "SoftServe")
print(worker)
print("*" * 50)

# Create and show Academy
acad_obj = Academy()
acad_obj.add_person(student)
acad_obj.add_person(worker)
acad_obj.show_all()

print(acad_obj)


from project.Person import Person
# import project.InvalidApiCall as InvalidApiCall


class Validator:
    def __init__(self):
        self.person_list = []

    def add_person(self, person):

        if self.is_id_unique(person):
            self.person_list.append(person)
            return True
        else:
            return False

    def is_id_unique(self, person):
        for item in self.person_list:
            if person.info["id"] == item.info["id"]:
                # put exception throwing here later
                # raise InvalidApiCall("Person already exists with id: "+str(person.info["id"]))
                return False
        return True


def main():
    p = Person(1, "a", "b")
    p1 = Person(2, "a", "b")
    v = Validator()
    print(v.add_person(p))
    print(v.add_person(p1))
    print(v.person_list)


if __name__ == '__main__':
    main()



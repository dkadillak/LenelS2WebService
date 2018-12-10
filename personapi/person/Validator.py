
from person import PersonObj


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
                raise Exception("Person already exists with id: "+str(person.info["id"]))
        return True


def main():
    p = PersonObj(1, "a", "b")
    p1 = PersonObj(1, "a", "b")
    v = Validator()
    print(v.add_person(p))
    print(v.add_person(p1))
    print(v.person_list)


if __name__ == '__main__':
    main()



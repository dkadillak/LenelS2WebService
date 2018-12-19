
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

    def does_id_exist(self, person_id):
        # making sure what's passed in isn't an int
        person_id = str(person_id)
        for x in range(0, self.person_list.__len__()):
            if self.person_list[x].info["id"] == person_id:
                return x

        return -1

    def does_filter_match(self, list_filter, index):
        if self.person_list[index].info["first_name"] == list_filter:
            return True
        elif self.person_list[index].info["last_name"] == list_filter:
            return True
        else:
            return False

    def create_list_by_filter(self, list_filter):
        list_filter = str(list_filter)
        matches = []
        for index in range(0, self.person_list.__len__()):
            if self.does_filter_match(list_filter, index):
                matches.append(self.person_list[index])

        return matches

def main():
    p = Person(1, "a", "b")
    p1 = Person(2, "c", "a")
    v = Validator()
    print(v.add_person(p))
    print(v.add_person(p1))
    # print(v.person_list)

    print(v.create_list_by_filter("c"))







if __name__ == '__main__':
    main()



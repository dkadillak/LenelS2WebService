
from project.Person import Person
import json
# import project.InvalidApiCall as InvalidApiCall


class Validator:
    def __init__(self):
        self.person_list = []   # storage for all created people when the server is running
        self.id_list = []   # id list is for quickly answering questions about id's being unique/existing

    def add_person(self, person):

        if self.is_id_unique(person):
            self.person_list.append(person)
            self.id_list.append(person.info["id"])
            return True
        else:
            return False

    def is_id_unique(self, person):

        if person.info["id"] in self.id_list:
            return False
        else:
            return True

    def does_id_exist(self, person_id):

        # making sure what's passed in isn't an int
        person_id = int(person_id)

        try:
            index = self.id_list.index(person_id)
            return index
        except ValueError:
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

    # updates only the fields which have changed (meaning none null)
    # validates that the new_id is still unique
    def modify_person(self, person_id, new_id, new_first, new_last):

        index = self.does_id_exist(person_id)
        if index != -1:
            if self.update_person(index, int(new_id), new_first, new_last):
                return True
            else:
                # if we reach this point, given id was not unique
                return False
        else:
            # if we reach this point, person that were trying to modify doesn't exist
            return False

    def update_person(self, index, new_id, new_first, new_last):
        # grabbing all the current information for the person
        person_id = self.person_list[index].info["id"]
        first_name = self.person_list[index].info["first_name"]
        last_name = self.person_list[index].info["last_name"]

        # updating only the fields that changed
        if self.did_id_change(person_id,new_id):
            if new_id in self.id_list:
                return False
            else:
                self.person_list[index].set_person_id(new_id)
                self.id_list[index] = new_id

        if self.did_first_name_change(first_name, new_first):
            self.person_list[index].set_first_name(new_first)

        if self.did_last_name_change(last_name, new_last):
            self.person_list[index].set_last_name(new_last)

        return True

    def did_id_change(self, person_id, new_id):
        if person_id == int(new_id) or new_id is None:
            return False
        else:
            return True

    def did_first_name_change(self, first_name, new_first):
        if first_name == new_first or new_first is None:
            return False
        else:
            return True

    def did_last_name_change(self, last_name, new_last):
        if last_name == new_last or new_last is None:
            return False
        else:
            return True

def main():
    p = Person(1, "a", "b")
    p1 = Person(2, "c", "a")
    v = Validator()
    v.add_person(p)
    v.add_person(p1)
    print(v.person_list)
    print(v.modify_person(1, 0, "mister", "kadillak"))

    print(v.person_list)







if __name__ == '__main__':
    main()



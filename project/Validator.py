
from project.Person import Person
import json
# import project.InvalidApiCall as InvalidApiCall


class Validator:
    def __init__(self):
        self.person_list = []   # storage for all created people when the server is running
        self.id_list = []   # id list is for quickly answering questions about id's being unique/existing

    def add_person(self, person):
        self.person_list.append(person)
        self.id_list.append(person.info["id"])

    # check if id is integer
    def validate_id(self, person_id):
        try:
            person_id = int(person_id)
        except ValueError:
            return "str_id"

        if person_id <= 0:
            return "inv_id_range"

        return True

    def remove_person(self, index):
        # update both the person list and id list
        self.person_list.remove(self.person_list[index])
        self.id_list.remove(self.id_list[index])

    def does_id_exist(self, person_id):
        # first validate id
        status = self.validate_id(person_id)
        if isinstance(status, str):
            return status
        else:
            # once id is valid, see if a person exists with that id
            try:
                # id exists
                index = self.id_list.index(int(person_id))
                return index
            except ValueError:
                # id does not exist
                return "id_doesn't_exist"

    def does_filter_match(self, list_filter, index):
        # check if the filter is contained in any substring of first/last name
        if list_filter in self.person_list[index].info["first_name"]:
            return True
        elif list_filter in self.person_list[index].info["last_name"]:
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

        # need to check if person_id is valid and exists
        # need to check if new id is valid and doesn't exist

        index = self.does_id_exist(person_id)
        new_id_code = self.does_id_exist(new_id)

        # if there is an error with the id passed in the body of the request, return error code
        if isinstance(new_id_code, str):
            return new_id_code

        # if there is an error with the person_id passed in via the URL, return error code
        if isinstance(index, str):
            return index

        elif isinstance(index, int):
            if self.update_person(index, int(new_id), new_first, new_last):
                return True
            else:
                # if we reach this point, given id in the request body is not unique
                return "id_exists"
        else:
            # if we reach this point, person that were trying to modify doesn't exist
            return "id_doesn't_exist"

    def update_person(self, index, new_id, new_first, new_last):
        # grabbing all the current information for the person
        person_id = self.person_list[index].info["id"]
        first_name = self.person_list[index].info["first_name"]
        last_name = self.person_list[index].info["last_name"]

        # updating only the fields that changed
        if self.did_id_change(person_id, new_id):
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
        if person_id == new_id:
            return False
        else:
            return True

    def did_first_name_change(self, first_name, new_first):
        if first_name == new_first or new_first == "":
            return False
        else:
            return True

    def did_last_name_change(self, last_name, new_last):
        if last_name == new_last or new_last == "":
            return False
        else:
            return True


def main():
    p = Person(1, "devin", "kadillak")
    p1 = Person(2, "steve", "joe")
    v = Validator()
    v.add_person(p)
    v.add_person(p1)
    # print(v.person_list)
    # print(v.id_list)
    # print(v.modify_person(1, 0, "mister", "kadillak"))
    # print(v.person_list)

    # print(isinstance("id", str))
    # print(isinstance(True, str))
    # v.remove_person(0)
    # print(v.person_list)
    #
    # print(v.id_list)

    # print(v.does_id_exist("hello"))
    print(v.modify_person(1, 3, "devin", "stinkerhead"))
    print(v.person_list)


if __name__ == '__main__':
    main()



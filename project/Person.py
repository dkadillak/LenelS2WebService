# python 3 implicitly extends from object
class Person:

    def __init__(self, person_id, first, last, debug=False):
        self.debug = debug
        self.info = {"id": person_id, "first_name": str(first), "last_name": str(last)}
        # could implement check to see if names are actually strings

    # overriding to string to return info dictionary
    def __repr__(self):
        if self.debug:
            print("calling __repr__")
        return str(self.info)

    def __str__(self):
        if self.debug:
            print("calling __str__")
        return str(self.info)

    # setters which will be used for PUT calls
    def set_person_id(self, new_id, debug=False):
        if debug:
            print('setting new id')
        self.info["id"] = new_id

    def set_first_name(self, new_first, debug=False):
        if debug:
            print('setting new first')
        self.info["first_name"] = new_first

    def set_last_name(self, new_last, debug=False):
        if debug:
            print('setting new last')
        self.info["last_name"] = new_last



if __name__ == '__main__':
    p1 = Person(1, "devin", "kadillak")
    p2 = Person(1, "ur", "mom")
    for item in p1.info:
        print(item+':', p1.info[item])

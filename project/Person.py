# python 3 implicitly extends from object
class Person:

    def __init__(self, person_id, first, last, debug=False):
        self.debug = debug
        self.info = {"id": str(person_id), "first_name": str(first), "last_name": str(last)}
        # could implement check to see if names are actually strings

    # overriding tostring to return info dictionary
    def __repr__(self):
        if self.debug:
            print("calling __repr__")
        return str(self.info)

    def __str__(self):
        if self.debug:
            print("calling __str__")
        return str(self.info)


if __name__ == '__main__':
    p1 = Person(1, "devin", "kadillak")
    p2 = Person(1, "ur", "mom")
    for item in p1.info:
        print(item+':', p1.info[item])

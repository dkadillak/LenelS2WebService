

# python 3 implicitly extends from object
class PersonObj:

    def __init__(self, person_id, first, last, debug=False):
        self.debug = debug
        self.info = {"id": person_id, "first_name": first, "last_name": last}

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
    p1 = PersonObj(1, "devin", "kadillak")
    p2 = PersonObj(1, "ur", "mom")
    print(p1)

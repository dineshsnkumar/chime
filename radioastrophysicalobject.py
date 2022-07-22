"""
Radio Physical Object
https://peps.python.org/pep-0008/#descriptive-naming-styles

"""
import json

class RadioPhysicalObject():
    valid_types = ["rrat", "frb", "neutron_star", "white_dwarf", "magneta"]

    def __init__(self, type_, dispersion, right_ascension, declination):
        self._type_ = type_
        self._dispersion = dispersion
        self._right_ascension = right_ascension
        self._declination = declination

    @property
    def dispersion(self):
        return self._dispersion

    @property
    def right_ascension(self):
        return self._right_ascension

    @property
    def declination(self):
        return self._declination

    @dispersion.setter
    def dispersion(self, value):
        self.dispersion = value

    @right_ascension.setter
    def right_ascension(self, value):
        self.right_ascension = value

    @declination.setter
    def declination(self, value):
        self.declination = value

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

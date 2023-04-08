from enum import Enum, auto


# TODO: move to python 3.11 and remove this shit
class StrEnum(str, Enum):
    def __new__(cls, *args):
        for arg in args:
            if not isinstance(arg, (str, auto)):
                raise TypeError(
                    "Values of StrEnums must be strings: {} is a {}".format(repr(arg), type(arg))
                )
        return super().__new__(cls, *args)

    def __str__(self):
        return self.value

    # The first argument to this function is documented to be the name of the
    # enum member, not `self`:
    # https://docs.python.org/3.6/library/enum.html#using-automatic-values
    def _generate_next_value_(name, *_):
        return name

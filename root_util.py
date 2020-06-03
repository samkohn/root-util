"""Utilities for reading and writing ROOT TTrees."""


__all__ = [
    "TreeBuffer",
    "int_value",
    "long_value",
    "unsigned_int_value",
    "float_value",
    "fetch_value",
    "assign_value",
]

from array import array


class TreeBuffer:
    def __str__(self):
        return str(self.__dict__)

    def copyTo(self, other):
        """Copy this TreeBuffer to an existing TreeBuffer.

        Copy the values in this TreeBuffer to an existing TreeBuffer set
        up with the same array attributes.
        """
        for attr, value in self.__dict__.items():
            otherArray = getattr(other, attr)
            for i, entry in enumerate(value):
                otherArray[i] = entry

    def clone(self, dest=None):
        """Clone this TreeBuffer to a new one.

        Create a new independent TreeBuffer with the same array
        attributes and values.
        """
        if dest is None:
            new = TreeBuffer()
        else:
            new = dest
        for attr, value in self.__dict__.items():
            setattr(new, attr, value[:])
        return new

    def clone_type(self, dest=None):
        """Clone the type/shape of this TreeBuffer but not the values.

        Create a new TreeBuffer with the same array attributes
        containing values of 0.
        """
        if dest is None:
            new = TreeBuffer()
        else:
            new = dest
        for attr, value in self.__dict__.items():
            setattr(new, attr, array(value.typecode, [0] * len(value)))
        return new


def int_value(length=1):
    return array("i", [0] * length)


def long_value(length=1):
    return array("l", [0] * length)


def unsigned_int_value(length=1):
    return array("I", [0] * length)


def float_value(length=1):
    return array("f", [0] * length)


def fetch_value(ttree, branch_name, type_cast):
    if type_cast == list:
        return list(getattr(ttree, branch_name))
    branch_object = ttree.GetBranch(branch_name)
    if "TBranchElement" in str(type(branch_object)):
        new_value = type_cast(branch_object.GetValue(0, 0))
    else:
        new_value = type_cast(getattr(ttree, branch_name))
    return new_value


def assign_value(buf_value, new_value, index=0):
    buf_value[index] = new_value

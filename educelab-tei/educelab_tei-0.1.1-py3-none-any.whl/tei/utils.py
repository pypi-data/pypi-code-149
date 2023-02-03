from abc import ABC, abstractmethod

from .constants import REQUIRED_FUNCTION, NAMESPACES
from .exceptions import TEILibError


class TEIElement(ABC):
    NAMESPACE = NAMESPACES['tei']

    @staticmethod
    @abstractmethod
    def tag():
        pass

    @staticmethod
    @abstractmethod
    def qname():
        pass

    @abstractmethod
    def generate_tree(self):
        pass

    @classmethod
    @abstractmethod
    def from_tree(cls, tree):
        pass


def _add_attribute_to_tree(tree, tag, attrib):
    if attrib is not None:
        tree.set(str(tag), str(attrib))
    return


def _add_namespace_attribute_to_tree(tree, qname, attrib):
    if attrib is not None:
        tree.set(qname, str(attrib))
    return


def _get_element_list(elem_list, cls, allow_none=True):
    output = []
    if elem_list is not None:
        if isinstance(elem_list, (list, tuple)):
            for item in elem_list:
                if isinstance(item, cls):
                    output.append(item)
                else:
                    raise TEILibError('Input type incorrect')
        elif isinstance(elem_list, cls):
            output.append(elem_list)
        else:
            raise TEILibError('Input type incorrect')
    else:
        if not allow_none:
            raise TEILibError('Value cannot be empty')
    return output


def _add_enum_value(value, enum, allow_none=True):
    if value is not None:
        value = str(value)
        if enum.has_value(value):
            return value
        else:
            raise ValueError('Value is not one of the possible options.')  # TODO print out allowed values
    elif not allow_none:
        raise ValueError('Value cannot be None')
    else:
        return None


def _add_tei_class(obj, expected_cls, allow_none=True, duck_type=True):
    if obj is not None:
        if isinstance(obj, expected_cls):
            return obj
        else:
            if duck_type:
                if hasattr(obj, REQUIRED_FUNCTION):
                    return obj
                else:
                    raise TypeError('Input type incorrect. Instance has to implement function ' +
                                    REQUIRED_FUNCTION)
            else:
                raise TypeError('Input type incorrect.')
    elif not allow_none:
        raise ValueError('Value cannot be None')
    else:
        return None


def _get_integer_value(value, allow_none=True):
    if value is not None:
        try:
            return int(value)
        except:
            raise ValueError('Parameter requires an integer value')
    elif not allow_none:
        raise ValueError('Value cannot be None')
    else:
        return None


def _get_string_value(value, allow_none=True):
    if value is not None:
        try:
            return str(value)
        except:
            raise ValueError('Parameter requires a string value')
    elif not allow_none:
        raise ValueError('Value cannot be None')
    else:
        return None


def _check_tag(tag: str, expected: str, ns: str = NAMESPACES['tei']) -> bool:
    if tag == expected or tag == '{' + ns + '}' + expected:
        return True
    else:
        return False

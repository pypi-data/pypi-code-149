from dataclasses import dataclass


@dataclass
class CerbeyraIndex:
    index: str
    risk_level: str
    explain: dict

    __ci_order = ['A+++', 'A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

    def __str__(self):
        """
        Defines the string representation for the CerbeyraIndex object.

        :return: the string representation.
        """
        return self.index

    def __eq__(self, other):
        """
        Makes it possible to verify the equality of two CerbeyraIndex object (based on the cerbeyra_index attribute).

        :param other: another CerbeyraIndex object
        :return: a boolean
        """
        return self.index == other.index

    def __gt__(self, other):
        """
        Makes it possible to verify whether a CerbeyraIndex object is greater than another
        (based on the cerbeyra_index attribute).

        :param other: another CerbeyraIndex object
        :return: a boolean
        """
        obj_index = self.__ci_order.index(self.index)
        other_index = self.__ci_order.index(other.index)
        return obj_index < other_index

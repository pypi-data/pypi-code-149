# Class Switch: Defines a switch that may be executed as many times as needed.
class Switch:
    """
    This class creates a switch structure in Python. It may be configured to manage a default case if necessary.

    An object of type Switch must be declared using at least one argument:

    - cases: <class 'dict'>. A dictionary composed of the conditions that the switch may match and their related switch values. A switch value may be whatever, from an integer to a function performing the action needed when its switch condition has been matched.

    There are also two optional arguments that may be provided when creating the object:

     - use_default_case: <class 'bool'>. Used to determine if a default case is necessary for the switch. By default its value is False.
     - default_case: The action to perform in the default case if use_default_case == True.

    METHODS:

     - exec: This method takes the desired choice as argument and returns the corresponding switch value.

     - add_case: This method takes a condition and a switch value, and creates a new switch case with them.

     - update_case: This method takes a condition used in one of the defined cases and a new switch value, that may be returned by the Switch when the execution matches the condition.

     - delete_case: This method deletes the introduced case from the object.

     - enable_default_case: This method sets the Switch object to use a default case when the execution does not match the defined ones. If the Switch object had this feature activated, nothing happens.

     - disable_default_case: This method sets the Switch object to return None when the execution does not match any the defined cases. If the Switch object was configured in such a way before using this method, nothing happens.

     - update_default_case: This method updates the default switch value to return, if the Switch object must return such a value when the execution does not match any of the defined cases.
    """

    def __init__(
        self,
        cases: dict,
        use_default_case: bool = False,
        default_case=None,
    ) -> None:
        # Check that the type of the arguments are correct.
        if cases.__class__ != dict:
            raise ValueError(
                "switch cases must be declared using a dict object {{case: action_to_perform}}, but {} object was given.".format(
                    cases.__class__
                )
            )
        if use_default_case.__class__ != bool:
            raise ValueError(
                "set use_default_case = True if you are interested in using a default case for the switch. {} object was given.".format(
                    use_default_case.__class__
                )
            )
        # Definition of the object attributes.
        self.__cases = cases
        self.__use_default_case = use_default_case
        self.__default_case = default_case

    def exec(self, choice):
        """
        Returns the selected choice of the switch.
        """
        if self.__use_default_case:
            return self.__cases.get(choice, self.__default_case)
        return self.__cases.get(choice)

    def add_case(self, new_condition, new_value):
        """
        This method allows to add a new execution case to the switch object.
        """
        # Check that the new case is not already part of the switch object.
        if new_condition in self.__cases.keys():
            raise ValueError(
                "The introduced condition is already part of the Switch. If you want to update the action, use update_case method instead."
            )
        self.__cases.setdefault(new_condition, new_value)

    def update_case(self, condition, new_value):
        """
        This method updates the switch value to perform when the input condition happens.
        """
        # Check that the case is already part of the switch object.
        if condition not in self.__cases.keys():
            raise ValueError(
                "The introduced condition is not part of the Switch. If you want to add a new case, use add_case method instead."
            )
        self.__cases[condition] = new_value

    def delete_case(self, condition):
        """
        This method deletes a case from the switch object.
        """
        if condition not in self.__cases.keys():
            raise ValueError(
                "The introduced condition is not part of the Switch object, so it is not possible to delete it."
            )
        self.__cases.pop(condition)

    def enable_default_case(self):
        """
        This method sets the Switch object to use a default case when the execution does not match the defined ones. If the Switch object had this feature activated, nothing happens.
        """
        self.__use_default_case = True

    def disable_default_case(self):
        """
        This method sets the Switch object to return None when the execution does not match any of the defined cases. If the Switch object was configured in such a way before using this method, nothing happens.
        """
        self.__use_default_case = False

    def update_default_case(self, new_value):
        """
        This method updates the default switch value to return, if the Switch object must return such a value when the execution does not match any of the defined cases.
        """
        self.__default_case = new_value

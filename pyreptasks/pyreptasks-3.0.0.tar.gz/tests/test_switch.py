# These tests are designed to proof that the Switch class acts as it is attended.

# Import of the switch class

from pyreptasks import Switch


# Definition of some simple functions to be called during the tests.
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def hello_world():
    return "Hello world!"


###################################################################################################
# Correct performance tests
###################################################################################################

# FIRST SWITCH. It will take 4 options [1,2,3,4] and the 4 functions defined
# above. If the switch choice is out of [1,2,3,4] it will returns the string "default case accessed".

# Test 1: Good performance, the switch returns exactly what is expected.


def test_1():
    my_switch = Switch(
        {1: add, 2: sub, 3: mul, 4: hello_world},
        use_default_case=True,
        default_case="default case accessed",
    )
    assert my_switch.exec(1)(3, 4) == 7  # 3+4 = 7
    assert my_switch.exec(2)(3, 4) == -1  # 3-4 = -1
    assert my_switch.exec(3)(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec(4)() == "Hello world!"  # Execution of hello_world function
    assert (
        my_switch.exec(32433323239424) == "default case accessed"
    )  # Otherwise, default case


# Test 2: We disable the default case and repeat the previous test, but making sure that the default case returns None this time (as the default_case is not activated).


def test_2():
    my_switch = Switch(
        {1: add, 2: sub, 3: mul, 4: hello_world},
        use_default_case=True,
        default_case="default case accessed",
    )
    my_switch.disable_default_case()
    assert my_switch.exec(1)(3, 4) == 7  # 3+4 = 7
    assert my_switch.exec(2)(3, 4) == -1  # 3-4 = -1
    assert my_switch.exec(3)(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec(4)() == "Hello world!"  # Execution of hello_world function
    assert (
        my_switch.exec(32433323239424) == None
    )  # Otherwise, default case, now deactivated


# SECOND SWITCH. Similar to the first one but this time there is not a default case in the constructor.

# Test 3: Testing the second switch...


def test_3():
    my_switch = Switch({"add": add, "sub": sub, 4.89: mul, 6: hello_world})
    assert my_switch.exec("add")(3, 4) == 7  # 3+4 = 7
    assert my_switch.exec("sub")(3, 4) == -1  # 3-4 = -1
    assert my_switch.exec(4.89)(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec(6)() == "Hello world!"  # Execution of hello_world function
    assert my_switch.exec(32433323239424) == None  # There is not a default case


# Test 4: We enable the default case. As there is not any default_case declared in the constructor, we have to add a new one using the related class method.


def test_4():
    my_switch = Switch({"add": add, "sub": sub, 4.89: mul, 6: hello_world})
    my_switch.enable_default_case()
    my_switch.update_default_case("This is the new default case")
    assert my_switch.exec("add")(3, 4) == 7  # 3+4 = 7
    assert my_switch.exec("sub")(3, 4) == -1  # 3-4 = -1
    assert my_switch.exec(4.89)(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec(6)() == "Hello world!"  # Execution of hello_world function
    assert my_switch.exec(32433323239424) == "This is the new default case"


# Test 5: We can now try to update the "add" condition. Instead of performing the addition of both numbers, it will compute a*b


def test_5():
    my_switch = Switch({"add": add, "sub": sub, 4.89: mul, 6: hello_world})
    my_switch.update_case("add", mul)
    assert my_switch.exec("add")(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec("sub")(3, 4) == -1  # 3-4 = -1
    assert my_switch.exec(4.89)(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec(6)() == "Hello world!"  # Execution of hello_world function
    assert my_switch.exec(32433323239424) == None


# Test 6: Now, we add a new condition to the switch using the add_case method :)


def test_6():
    my_switch = Switch({"add": add, "sub": sub, 4.89: mul, 6: hello_world})
    my_switch.add_case(("My", "Tuple"), 567489)
    assert my_switch.exec("add")(3, 4) == 7  # 3+4 = 7
    assert my_switch.exec("sub")(3, 4) == -1  # 3-4 = -1
    assert my_switch.exec(4.89)(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec(6)() == "Hello world!"  # Execution of hello_world function
    assert my_switch.exec(("My", "Tuple")) == 567489
    assert my_switch.exec(32433323239424) == None


# Test 7: And we repeat de previous test but we also delete the case, so now the Switch would call the default case, but it is not activated in this case, so we will get None


def test_7():
    my_switch = Switch({"add": add, "sub": sub, 4.89: mul, 6: hello_world})
    my_switch.add_case(("My", "Tuple"), 567489)
    my_switch.delete_case(("My", "Tuple"))
    assert my_switch.exec("add")(3, 4) == 7  # 3+4 = 7
    assert my_switch.exec("sub")(3, 4) == -1  # 3-4 = -1
    assert my_switch.exec(4.89)(3, 4) == 12  # 3*4 = 12
    assert my_switch.exec(6)() == "Hello world!"  # Execution of hello_world function
    assert my_switch.exec(("My", "Tuple")) == None
    assert my_switch.exec(32433323239424) == None


###################################################################################################
# CONSTRUCTOR ERRORS. Tests of how the class constructor throw exceptions if the arguments
# are not well passed.
###################################################################################################

# Test 8: The constructor does not receive the mandatory arguments -> TypeError


def test_8():
    try:
        Switch(use_default_case=True)
    except TypeError:
        pass


# Test 9: The switch's cases argument is not a dictionary -> ValueError


def test_9():
    try:
        Switch([2, 3, 4])
    except ValueError:
        pass


# Test 10: The optional argument use_default_case is not a boolean -> ValueError


def test_10():
    try:
        Switch({3: add, 4: hello_world}, use_default_case=54)
    except ValueError:
        pass


#########################################################################################################################
# METHOD ERRORS. Test that the methods defined in a Switch object raise the defined exceptions.
#########################################################################################################################


def test_11():
    my_switch = Switch({"add": add, "sub": sub, 4.89: mul, 6: hello_world})
    ## add_case exception
    try:
        my_switch.add_case("add", 234)
    except ValueError:
        pass
    ## update_case exception
    try:
        my_switch.update_case(123, add)
    except ValueError:
        pass
    ## delete_case exception
    try:
        my_switch.delete_case(123)
    except ValueError:
        pass

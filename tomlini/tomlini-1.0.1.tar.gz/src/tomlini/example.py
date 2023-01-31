import tomlini

@tomlini.toml_init
class MyClass:
    def __init__(self, v1):
        self.v1 = v1


if __name__ == "__main__":
    mc = MyClass.load_from_toml_string(
        'v1 = 1'
    )

    print(mc.v1) # will output '1'
import pathlib


__all__ = ['WEAK_PASSWORDS']


def _load_weak_passwords():
    passwords = []
    path = pathlib.Path(__file__).resolve().parent.parent / 'etc/passwords.txt'
    with open(path, 'r') as f:
        for row in f.readlines():
            passwords.append(row.strip().lower())
    return frozenset(passwords)


WEAK_PASSWORDS = _load_weak_passwords()

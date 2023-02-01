from itertools import chain, repeat
import numpy as np
import pandas as pd
import pkg_resources


def design_matrix(n_runs: int):
    """
    Generate the design matrix, Table 1 of Chen, Sun and Wu (1993), for a
    specific run size.

    Parameters
    ----------
    n_runs : int
        Number of runs.

    Returns
    -------
    mat : np.array
        Design matrix.

    """
    # Init the matrix
    n_bf = int(np.log2(n_runs))
    mat = np.zeros((n_bf, n_runs - 1))
    cols = list(range(n_runs - 1))

    # Fill the matrix
    for i in cols:
        col_num = i + 1
        # Power of 2 case
        if np.log2(col_num) % 1 == 0:
            k = int(np.log2(col_num))
            mat[k, i] = 1
        # Alternative case
        s = np.binary_repr(col_num, width=n_bf)
        mat[:, i] = list(map(int, s[::-1]))
    return mat


def load_tables():
    """
    Return a dataframe with all designs from the Chen, Sun and Wu (1993) paper.

    Contains the following fields: n.runs, index, n.cols, n.added, design.rank, cols,
    wlp, clear.2fi

    Returns
    -------
    pd.DataFrame
        Table of all designs.

    """
    filepath = pkg_resources.resource_stream(__name__, "data/tables.csv")
    df = pd.read_csv(filepath, header=0, sep=",")
    df["u_id"] = df["n.runs"].astype(str) + "." + df["index"]
    return df.set_index("u_id")


def basic_factor_matrix(n_bf: int):
    """
    Generate a full design matrix that only contains basic factors.

    Parameters
    ----------
    n_bf : int
        Number of basic factors.

    Returns
    -------
    mat : np.array
        Basic factors matrix.

    """
    mat = np.zeros((2 ** n_bf, n_bf))
    for i in range(n_bf):
        a = 2 ** n_bf // (2 ** (i + 1))
        b = 2 ** n_bf // (2 * a)
        col_list = repeat([0] * a + [1] * a, b)
        col = list(chain(*col_list))
        mat[:, i] = col
    return mat


def get_design(n_runs: int, index: str):
    """
    Generate the full design matrix given the number of runs and the specific
    index of the design.

    Parameters
    ----------
    n_runs : int
        Number of runs.
    index : str
        Index of the design. Equivalent to the first column in the tables of
        Chen, Sun and Wu (1993)

    Raises
    ------
    ValueError
        Number of runs must be a power of 2.
        Index must correspond to a design in the paper.

    Returns
    -------
    mat: np.array
        Full design matrix.

    Examples
    --------

    Generate the design matrix of the 16-run design with index "8-4.1" from Table 2
    of Chen, Sun and Wu (1993)

    >>> get_design(16, "8-4.3")
    array([[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 1, 1],
           [0, 0, 0, 1, 1, 0, 0, 1],
           [0, 0, 0, 1, 1, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 0],
           [0, 1, 1, 0, 0, 1, 0, 1],
           [0, 1, 1, 1, 1, 0, 1, 1],
           [0, 1, 1, 1, 1, 1, 0, 0],
           [1, 0, 1, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 1, 1, 1, 1],
           [1, 0, 1, 1, 0, 0, 0, 1],
           [1, 0, 1, 1, 0, 1, 1, 0],
           [1, 1, 0, 0, 1, 0, 1, 0],
           [1, 1, 0, 0, 1, 1, 0, 1],
           [1, 1, 0, 1, 0, 0, 1, 1],
           [1, 1, 0, 1, 0, 1, 0, 0]])

    """
    # Test if nbr of runs is a power of two
    log2_runsize = np.log2(n_runs)
    if log2_runsize % 1 != 0:
        raise ValueError("Number of runs must be a power of 2")
    else:
        n_bf = int(log2_runsize)
    # Load the tables
    table = load_tables()
    # Build index
    design_index = str(n_runs) + "." + index
    # Retrieve information
    try:
        design_info = table.loc[design_index]
    except KeyError:
        print(index, "is not a valid design index for ", n_runs, "-run designs")
        return None
    # Extract column numbers
    basic_factors = [2 ** i for i in range(n_bf)]
    added_factors = list(map(int, design_info["cols"].split(",")))
    columns = [i - 1 for i in basic_factors + added_factors]
    columns.sort()
    # Build basic factor matrix
    bf_mat = basic_factor_matrix(n_bf)
    # Build design matrix
    design_mat = design_matrix(n_runs)
    specific_design_mat = design_mat[:, columns]
    # Matrix multiplication
    mat = (np.matmul(bf_mat, specific_design_mat) % 2).astype(int)
    return mat


def get_wlp(n_runs: int, index: str):
    """
    Retrieve the word length pattern (WLP) starting on length 3 words for
    a given run size and design index. For 64-run design, the (WLP) starts
    on length 4 words.

    Parameters
    ----------
    n_runs : int
        Number of runs
    index : str
        Index of the design. Equivalent to the first column in the tables of
        Chen, Sun and Wu (1993)

    Returns
    -------
    wlp : List[int]
        Word length pattern

    Raises
    ------
    ValueError
        Number of runs must be a power of 2.
        Index must correspond to a design in the paper.

    Example
    -------

    Retrieve the Word length pattern of the 32-run design with index "17-12.3",
    presented in Table 3 of Chen, Sun and Wu (1993)

    >>> get_wlp(32,"17-12.3")
    [18, 95, 192, 354]

    """
    # Test if nbr of runs is a power of two
    if np.log2(n_runs) % 1 != 0:
        raise ValueError("Number of runs must be a power of 2")
    # Load the tables
    table = load_tables()
    # Build index
    design_index = str(n_runs) + "." + index
    # Retrieve information
    try:
        design_info = table.loc[design_index]
    except KeyError:
        print(index, "is not a valid design index")
        return None
    # Extract WLP string
    wlp_str = design_info["wlp"]
    wlp = list(map(int, wlp_str.split(",")))
    return wlp


def get_cfi(n_runs: int, index: str):
    """
    Retrieve the number of clear two-factor interactions for a given run size and
    design index.

    A two-factor interaction is considered clear if it is not aliased with any other
    main effect or two-factor interaction.

    Parameters
    ----------
    n_runs : int
        Number of runs
    index : str
        Index of the design. Equivalent to the first column in the tables of
        Chen, Sun and Wu (1993)

    Returns
    -------
    cfi : int
        Number of clear two-factor interactions

    Raises
    ------
    ValueError
        Number of runs must be a power of 2.
        Index must correspond to a design in the paper

    Example
    -------

    Retrieve the number of clear two-factor interaction in the 64-run design with index
    "11-5.2", presented in Table 4 of Chen, Sun and Wu (1993)

    >>> get_cfi(64,"11-5.2")
    25

    """
    # Test if nbr of runs is a power of two
    if np.log2(n_runs) % 1 != 0:
        raise ValueError("Number of runs must be a power of 2")
    # Load the tables
    table = load_tables()
    # Build index
    design_index = str(n_runs) + "." + index
    # Retrieve information
    try:
        design_info = table.loc[design_index]
    except KeyError:
        print(index, "is not a valid design index")
        return None
    # Extract clear 2fi number
    cfi = int(design_info["clear.2fi"])
    return cfi


def num2word(n: int) -> str:
    """Give the generator corresponding to a given column number.
    A generator is a letter representation of an interaction between two or more basic
    factors.

    Parameters
    ----------
    n : int
        Column number

    Returns
    -------
    gen : str
        Corresponding generator

    Raises
    ------
    ValueError
        Column number must be a positive integer

    Examples
    --------
    Check to which generator corresponds column number 11.
    Eleven can be decomposed in powers of two: 1, 2 and 8, so the corresponding
    generator must contain 'a', 'b' and 'd'.

    >>> num2word(11)
    'abd'

    """
    if (n < 1) or not isinstance(n, int):
        raise ValueError("Number must be a positive integer")
    gen = "".join([chr(97 + i) for i, x in enumerate(bin(n)[2:][::-1]) if int(x)])
    return gen


def word2num(w: str) -> int:
    """Give the generator corresponding to the given column number.
    The generator does not contain the letter representing the added factor itself,
    but only the letters representing the basic factors forming the interaction.

    Parameters
    ----------
    w : str
        Generator

    Returns
    -------
    num : int
        Column number

    Raises
    ------
    ValueError
        Generator must only contain lowercase letters from a to z

    Examples
    --------
    Which column number is equivalent to the generator 'abc' ?

    >>> word2num('abc')
    7

    """
    if any([(ord(i) < 97 or ord(i) > 122) for i in w]):
        raise ValueError("Generator must only contain lowercase letters")
    letter_numbers = [ord(i) - 97 for i in w]
    bin_num = ["0"] * (max(letter_numbers) + 1)
    for i in letter_numbers:
        bin_num[i] = "1"
    num = int("".join(bin_num[::-1]), 2)
    return num


if __name__ == "__main__":
    pass

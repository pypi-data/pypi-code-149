import os

import pandas as pd


def carregar_parametros(parametros):

    # carrega os parâmetros localizado na pasta "parametros"
    diretorio = os.path.dirname(__file__)
    diretorio = os.path.join(diretorio, "parametros")
    file = parametros + ".csv"
    df_parametro = pd.read_csv(os.path.join(diretorio, file), ";")
    pd.set_option("display.max_columns", None)
    df_parametro["PL"] = df_parametro["PL"].str.replace(",", ".", regex=False)
    df_parametro["PH"] = df_parametro["PH"].str.replace(",", ".", regex=False)

    return df_parametro

import pandas as pd


def make_summary_maya_2022_number_of_nest_marked(
    k9_data, start_date="2022-01-01", end_date="2023-01-29"
):
    nest_marked_by_maya_in_2022 = count_nest(k9_data, start_date, end_date)
    return (
        nest_marked_by_maya_in_2022.groupby("Nombre_k9", as_index=False)
        .agg(Conteo=("Tipo_de_rastro", "count"))
        .rename(columns={"Nombre_k9": "Unidad_K9"})
    )


def count_nest(k9_data, start_date, end_date) -> pd.DataFrame:
    k9_name = "Maya"
    only_maya = filter_k9(k9_name, k9_data)
    number_of_nest = filter_dates(only_maya, start_date, end_date)
    return filter_nest(number_of_nest)


def filter_dates(k9_data: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    filtered_df = k9_data.loc[(k9_data.Fecha <= end_date) & (k9_data.Fecha >= start_date)]
    return filtered_df


def filter_k9(k9_name: str, k9_data: pd.DataFrame) -> pd.DataFrame:
    return k9_data.loc[k9_data.Nombre_k9 == k9_name]


def filter_nest(k9_data: pd.DataFrame) -> pd.DataFrame:
    return k9_data.loc[k9_data.Tipo_de_rastro == "MD"]

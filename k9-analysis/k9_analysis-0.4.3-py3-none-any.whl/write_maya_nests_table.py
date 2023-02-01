from .count_burrows_detection import make_summary_maya_2022_number_of_nest_marked

import pandas as pd
import typer


app = typer.Typer()


@app.command()
def write_maya_nests_table(start_date, end_date, input_path, output_path):
    k9_data = pd.read_csv(input_path)
    summary = make_summary_maya_2022_number_of_nest_marked(k9_data, start_date, end_date)
    summary.to_csv(output_path, index=False)

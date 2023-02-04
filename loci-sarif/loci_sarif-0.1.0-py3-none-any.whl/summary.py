import click
import loci_sarif.utils as utils


@click.command()
@click.option("-f", "--input-file",
              prompt="SARIF JSON file",
              help="The SARIF file with the output of a scan",
              required=True,
              type=str)
def summary(input_file):
    """Summarize a SARIF file"""
    results_list = utils.open_sarif_file_and_get_results(input_file)

    utils.print_info(f"Summary for Results of [bold]{input_file}[/bold]:")
    total_results = len(results_list)
    utils.print_info(f"  Total issues: {total_results}")
    utils.print_info("-----------------------------------------------")

    results_by_sev_dict = {}
    results_by_sev_dict["error"] = []
    results_by_sev_dict["warning"] = []
    results_by_sev_dict["note"] = []

    for result in results_list:
        results_by_sev_dict[result.severity].append(result)

    for current_sev in ["error", "warning", "note"]:
        utils.print_info(f"  {current_sev.capitalize()}-severity issues: {len(results_by_sev_dict[current_sev])}")

        result_count = {}
        for result in results_by_sev_dict[current_sev]:
            try:
                result_count[result.ruleid]
            except KeyError:
                result_count[result.ruleid] = 0
            result_count[result.ruleid] += 1

        for w in sorted(result_count, key=result_count.get, reverse=True):
            utils.print_info(f"    x[bold]{result_count[w]}[/bold] {w}")

        utils.print_info("----------------------------------------------")

    utils.print_success("Results summarized.")

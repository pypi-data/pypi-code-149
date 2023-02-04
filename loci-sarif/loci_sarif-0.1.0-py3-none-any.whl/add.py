import click
import os
from rich.progress import Progress
import loci_sarif.utils as lutils


@click.command()
@click.option("-f", "--input-file",
              prompt="SARIF JSON file",
              help="The SARIF file with the output of a scan",
              required=True,
              type=str)
@click.option("-i", "--imports",
              help="Specific vulnerabilities or severities (comma separated) to import",
              required=True,
              type=str,
              default="error,warning,note")
def add(input_file, imports):
    """Process a SARIF file and add results to Loci Notes"""

    lutils.print_info("Getting directory project information...")
    project_id, project_name = lutils.get_project_id_from_config_in_dir(os.getcwd())
    if project_id is None or project_name is None:
        lutils.print_error("Unable to determine associated project. To correct this, run this under a directory "
                           "associated with a Loci Notes project.")
        quit(-1)
    lutils.print_success(f"Using [bold]{project_name}[/bold].")

    results_list = lutils.open_sarif_file_and_get_results(input_file)

    imports_list = imports.split(",")

    for i in range(len(imports_list)):
        # Remove whitespace, lowercase all, remove underscores
        imports_list[i] = imports_list[i].strip().lower().replace("_", " ")

    imported_severities_list = []
    if "error" in imports_list:
        imported_severities_list.append("error")
    if "warning" in imports_list:
        imported_severities_list.append("warning")
    if "note" in imports_list:
        imported_severities_list.append("note")

    # First count up total number of results to get a semi-accurate count of the results for the progress bar
    valid_results_found = 0
    for result in results_list:
        if result.ruleid.lower() in imports_list or result.severity.lower() in imported_severities_list:
            valid_results_found += 1

    if valid_results_found == 0:
        lutils.print_error("No results were found for the given imports. See the [bold]summary[/bold]"
                           " for valid vulnerabilities, or use 'Error', 'Warning', and 'Note' "
                           "to import by severity.")
        quit(-1)

    with Progress() as progress_bar:
        task = progress_bar.add_task(f"Importing {valid_results_found} results...", total=valid_results_found)

        for result in results_list:
            if result.ruleid.lower() in imports_list or result.severity.lower() in imported_severities_list:

                # Send the info to the LN server for the result
                new_note = {}
                new_note["artifact_descriptor"] = result.get_artifact()
                new_note["submission_tool"] = result.tool
                new_note["note_type"] = "LOG"
                new_note["contents"] = "**Security Issue Detected**\n\n"
                new_note["contents"] += "**Rule ID** - " + result.ruleid + "\n"
                new_note["contents"] += "**Severity** - " + result.severity.capitalize()
                new_note["contents"] += "**Messgae** - " + result.message

                # Detection and prevention of duplicate notes is handled by the server.
                lutils.loci_api_req(f"/api/projects/{project_id}/notes", method="POST",
                                    data=new_note, show_loading=False)

                progress_bar.update(task, advance=1)

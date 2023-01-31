"""Entry point for this project, runs the project code based on the cli command
that invokes this script."""

# Import code belonging to this project.


from .arg_parser.arg_parser import parse_cli_args
from .arg_parser.process_args import process_args

DEFAULT_OUTPUT_PATH = "output"


# Parse command line interface arguments to determine what this script does.
ARGS = parse_cli_args()
process_args(ARGS, default_output_path=DEFAULT_OUTPUT_PATH)

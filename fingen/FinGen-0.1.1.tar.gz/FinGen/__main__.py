import argparse
from .FindingsGenerator import FinGen 

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--title",
        required=True,
        action='append',
        help="Finding Title",
    )
    parser.add_argument(
        "--api_key",
        type=str,
        required=True,
        help="OpenAI API key",
    )
    return parser

def main(args):
    FinGen.CreateFinding(args.api_key, args.title)

if __name__ == "__main__":
    main(get_parser().parse_args())
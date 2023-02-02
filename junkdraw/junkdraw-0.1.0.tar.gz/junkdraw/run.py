import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

from junkdraw import create_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate random (or empty) file(s)")
    parser.add_argument("--path", type=str, help="Path to save the generated file")
    parser.add_argument("--size", type=int, help="Size of the generated file in bytes")
    parser.add_argument(
        "--min-size", type=int, help="Minimum size of the generated file in bytes"
    )
    parser.add_argument(
        "--max-size", type=int, help="Maximum size of the generated file in bytes"
    )
    parser.add_argument("--count", type=int, help="Number of files to generate")
    parser.add_argument(
        "--total-size", type=int, help="Cumulative size of all files generated in bytes"
    )
    parser.add_argument(
        "--max-children",
        type=int,
        default=None,
        help="Create no more than this many files or directories in any one directory",
    )
    parser.add_argument(
        "--random", action="store_true", help="Fill files with random data"
    )
    return parser.parse_args()


@dataclass
class ScriptParams:
    path: Path = None
    count: int = 1
    size: Tuple[int, int] = (0, 0)
    random: bool = False
    max_children: Optional[int] = None

    @property
    def description(self) -> str:
        """A descriptive string suitable to use as a directory name."""
        size = (
            f"{self.size[0]}"
            if self.size[0] == self.size[1]
            else f"{self.size[0]}-{self.size[1]}"
        )
        desc = f"{size}x{self.count}"
        desc += "t" if self.max_children else ""
        desc += "r" if self.random else ""
        return desc

    @staticmethod
    def from_args(args) -> "ScriptParams":
        params = ScriptParams(
            path=Path(args.path) if args.path else None,
            count=args.count or 1,
            size=(args.min_size or args.size or 0, args.max_size or args.size or 0),
            random=args.random,
            max_children=args.max_children,
        )
        if args.total_size:
            if args.count:
                size = args.total_size // args.count
                params.size = (size, size)
            else:
                params.count = 2 * args.total_size / (params.size[0] + params.size[1])

        params.path = params.path or Path.cwd() / "junkdrawer" / params.description

        return params


def main():
    params = ScriptParams.from_args(parse_args())
    create_files(
        root=params.path,
        count=params.count,
        min_size=params.size[0],
        max_size=params.size[1],
        random=params.random,
        max_children=params.max_children,
    )


if __name__ == "__main__":
    main()

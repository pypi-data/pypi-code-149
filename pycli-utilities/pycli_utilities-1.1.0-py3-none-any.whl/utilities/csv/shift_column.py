"""
    Copyright (c) 2022 Vishv Patel (https://github.com/itsthevp)

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from time import time

from source.utilities.csv.cli import CSVUtils


class ShiftColumnCSV(CSVUtils):
    prog = "csv-shift-column"
    usage = "%(prog)s file from_location to_location [options]"
    description = "This utility is designed to shift (not swap) particular column of a CSV file."

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "from_location",
            metavar="from_location",
            type=int,
            help="Column's number which needs to be shifted (Starting from 1).",
        )
        self.parser.add_argument(
            "to_location",
            metavar="to_location",
            type=int,
            help="Column's number where column needs to be placed (Starting from 1).",
        )
        self.parser.add_argument(
            "--output-file",
            type=str,
            metavar="",
            dest="output",
            help="Output CSV file name",
            default=f"column-shifted-csv-{int(time())}.csv",
        )

    def main(self) -> None:
        reader = self.read_from_csv(self.args.input)
        writer = self.write_to_csv(self.args.output)
        row = self.get_next_row(reader)
        col_count = len(row)

        # Validating shifting locations
        if (
            not 1 <= self.args.from_location <= col_count
            and not 1 <= self.args.to_location <= col_count
        ):
            self.log("Invalid shift locations passed !!")
            raise SystemExit()

        while row:
            shift_content = row.pop(self.args.from_location - 1)
            row.insert(self.args.to_location - 1, shift_content)
            writer.writerow(row)
            row = self.get_next_row(reader)


def run() -> None:
    ShiftColumnCSV().run()


if __name__ == "__main__":
    run()

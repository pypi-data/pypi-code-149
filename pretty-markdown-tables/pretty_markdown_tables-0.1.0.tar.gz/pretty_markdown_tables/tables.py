import pandas as pd
from io import StringIO
from pretty_html_table import build_table
import re
import markdown2
from loguru import logger


class ConvertMarkdownTables:
    def __init__(self, markdown: str):
        self.markdown = markdown

    def convert(self) -> str:
        """Convert Markdown table to HTML table

        Returns:
        str: HTML string
        """
        lines = re.split("\n", self.markdown)
        lines = [line.lstrip() for line in lines]

        output = []
        in_table = False
        for line in lines:
            logger.debug(line)
            if line.startswith("|") and not in_table:
                # Table Found
                table_data = [line]
                in_table = True
            elif line.startswith("|-") and in_table:
                # Ignore table separator line
                pass
            elif line.startswith("|") and in_table:
                # Append table lines
                table_data.append(line)
            elif not line.startswith("|") and in_table:
                # End of table, convert markdown to HTML using pretty_html_table
                html = ConvertMarkdownTables.convert("\n".join(table_data))
                output.append(str(html))

                in_table = False
                output.append(line)
            else:
                output.append(line)

        # Convert Markdown to HTML
        converter = markdown2.Markdown(extras=[
            "tables",
            "fenced-code-blocks",
            "cuddled-lists",
            "numbering",
            "strike",
            "pyshell",
            "footnotes",
            "mermaid"
        ])

        return converter.convert("\n".join(output))

    @staticmethod
    def convert_table(markdown_table: str,
                      color: str = 'blue_light',
                      font_size: str = 'medium',
                      font_family: str = 'Century Gothic, sans-serif',
                      text_align: str = 'left',
                      width: str = 'auto',
                      index: bool = False,
                      even_color: str = 'black',
                      even_bg_color: str = 'white',
                      odd_bg_color: str = None,
                      border_bottom_color: str = None,
                      escape: bool = True,
                      width_dict: list = [],
                      padding: str = "0px 20px 0px 0px",
                      float_format: str = None,
                      conditions={}) -> str:
        """ Convert Markdown table to HTML table using pretty_html_table

        Args:
        markdown_table (str): The markdown table string
        color (str): Color of table
        font_size (str): Font size of table
        font_family (str): Font family of table
        text_align (str): Alignment of text in the table cells
        width (str): Width of table
        index (bool): Display index or not
        even_color (str): Text color for even rows
        even_bg_color (str): Background color for even rows
        odd_bg_color (str): Background color for odd rows
        border_bottom_color (str): Bottom border color for the table
        escape (bool): Escape HTML characters or not
        width_dict (list): List of column widths
        padding (str): Padding for cells
        float_format (str): Formatting string for floating point numbers
        conditions (dict): Dictionary of condition-format mapping

        Returns:
        str: HTML string
        """

        df = pd.read_csv(StringIO(markdown_table), sep='|').dropna(axis=1, how='all')

        html = build_table(df,
                           color=color,
                           font_size=font_size,
                           font_family=font_family,
                           text_align=text_align,
                           width=width,
                           index=index,
                           even_color=even_color,
                           even_bg_color=even_bg_color,
                           odd_bg_color=odd_bg_color,
                           border_bottom_color=border_bottom_color,
                           escape=escape,
                           width_dict=width_dict,
                           padding=padding,
                           float_format=float_format,
                           conditions=conditions
                           )

        return html

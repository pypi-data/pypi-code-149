# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""A simple replacement for gee pee elled licensed tabulate package."""
from io import StringIO

"""
+--------+-------+
| item | qty |
+========+=======+
| spam | 42 |
+--------+-------+
| eggs | 451 |
+--------+-------+
| bacon | 0 |
+--------+-------+

"""

MAPPING_DICT = {
    "html": {
        "tablestart": "<table>",
        "tableend": "</table>",
        "headingstart": "<thead>",
        "headingend": "</thead><tbody>",
        "headingpreamble": '<th style="text-align: right;">',
        "datapreamble": '<td style="text-align: right;">',
        "datapostamble": "</td>",
        "headingpostamble": "</th>",
        "rowstart": "<tr>",
        "rowend": "</tr>",
        "rowend1": "</tr>",
        "bodyend": "</tbody></table>",
    },
    "grid": {
        "tablestart": "",
        "tableend": "",
        "headingstart": "+--------",
        "headingend": "+========",
        "headingpreamble": "|",
        "datapreamble": "|",
        "datapostamble": "|",
        "headingpostamble": "|",
        "rowstart": "",
        "rowend": "",
        "rowend1": "+---------",
        "bodyend": "",
    },
}


def _generic(data, headers, tablefmt="html"):
    tags = MAPPING_DICT[tablefmt]
    ans = StringIO()
    ans.write(tags["tablestart"])
    ans.write(tags["headingstart"])
    ans.write(tags["rowstart"])
    for header in headers:
        ans.write(tags["headingpreamble"])
        ans.write(str(header))
        ans.write(tags["headingpostamble"])
    ans.write(tags["rowend"])
    ans.write(tags["headingend"])
    for row in data:
        ans.write(tags["rowstart"])
        for element in row:
            ans.write(tags["datapreamble"])
            ans.write(str(element))
            ans.write(tags["datapostamble"])
        ans.write(tags["rowend1"])
    ans.write(tags["bodyend"])
    if tablefmt == "grid":
        ans = (
            ans.getvalue()
            .replace("||", "|")
            .replace(
                tags["headingstart"],
                "{}+\n".format(tags["headingstart"] * len(headers)),
            )
            .replace(
                tags["headingend"], "{}+\n".format(tags["headingend"] * len(headers))
            )
            .replace(tags["rowend1"], "{}+\n".format(tags["rowend1"] * len(headers)))
        )
        return ans
    else:
        return ans.getvalue()


def tabulate(data, headers=None, tablefmt="html", stralign="notused_legacy"):

    """
    Returns a string formatted according to tablefmt (currenty supports only 'html' or 'grid')

    Args:
        data (list, required): list of list containing data with each inner list becoming a row.
        headers (list, required): list of strings and length equal to the number of columns
            in the data.
        tablefmt (str, optional): 'html' or 'grid'
    """
    if headers is None:
        raise TypeError(
            """tabulate() missing 1 required positional argument: 'headers'. Provide 'header' """
            + """argument as a list of strings and length equal to the number of columns """
            + """with unique column names in resulting table."""
        )
    if len(headers) != len(data[0]):
        raise ValueError(
            "Length of 'headers' and 'data' is not matching. Length of 'headers' is {} whereas length of 'data' (1st row) is {}.".format(
                str(len(headers)), str(len(data[0]))
            )
        )
    if tablefmt in ["html", "grid"]:
        return _generic(data, headers, tablefmt)
    else:
        raise Exception("{} format is currently not supported".format(tablefmt))

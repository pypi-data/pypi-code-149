#!/usr/bin/env python3
# Filename: tools.py

import km3dia
import datetime
import re

"""
Collection of DOM and DU integration tools using DIA information
"""


def get_promisID(DOM_UPI):
    """Get promisID mapping for a specific DOM"""

    db = km3dia.DBManager(container="pd")
    df = db.get_SQL(
        f"SELECT * FROM DOM_INTEGRATION INNER JOIN Part_data ON DOM_INTEGRATION.PRODUPI = Part_data.PRODUPI  WHERE DOM_INTEGRATION.DOMUPI='{DOM_UPI}' AND LOCATE('3.4.2.3', Part_data.PRODUPI) > 0"
    )
    df = df.pivot(
        index=["DOMUPI", "POS", "PRODUPI"], columns="DataName", values="Datum"
    )
    df = df.reset_index()

    def POS2chanID(POS):
        chan = POS.split("(")[1]
        chan = chan.replace(")", "")
        chan = int(chan)
        return chan

    df["ChanID"] = df["POS"].apply(POS2chanID)
    df = df.set_index(["DOMUPI", "ChanID"]).sort_index()

    df["PMT_PROMISID"] = df["PMT_PROMISID"].str.replace("\t", "")
    return df


def save_opt_file(DOM_UPI, outfile, default_threshold=47):
    """Save to disk an optfile generated from DIA DB"""

    df = get_promisID(DOM_UPI)

    with open(outfile, "w") as fout:
        fout.write("# Optics configuration storage\n")
        fout.write("# Generated using km3dia\n")
        fout.write(f"# {datetime.datetime.now()}\n")
        fout.write(f"# {DOM_UPI}\n")

        for (DOM_UPI, ChanID), row in df.iterrows():
            fout.write(f"ch{ChanID}.id={row.PMT_PROMISID}\n")
            fout.write(f"ch{ChanID}.hv={row.PMT_HIGHVOLT}\n")
            fout.write(f"ch{ChanID}.ths={default_threshold}\n")

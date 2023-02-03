#-----------------------------------
# Imports
#-----------------------------------

import locale
import csv
from typing import List

from muphyn.packages.core.utils.log_manager import LogManager

#-----------------------------------
# Functions
#-----------------------------------

def _init_csv_box (box, simulation_params) -> List :
    box['values'] = []
    box['point_count'] = 0

    titles = []
    titles.append('Time')
    v = 0
    for input in box.inputs :
        titles.append(str(v))
        v += 1
    box['values'].append(titles)

def _function_csv_box (box, event_) -> List :

    if box['copy_timing_from_simulation'] is True or (event_.timing > box['start_time'] and event_.timing < box['stop_time']) :
        lst = []
        lst.append(event_.timing)

        for input in box.inputs :
            lst.append(input.value)

        box['point_count'] = box['point_count'] + 1
        box['values'].append(lst)

    return []

def _end_csv_box (box) -> None : 
    LogManager().info('decimal delimiter : ', locale.localeconv()["decimal_point"])

    with open(box['file_name'], 'w', newline=box['new_line']) as csv_file : 
        writer = csv.writer(csv_file, delimiter=box['delimiter'], quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(box['values'])

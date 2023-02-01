"""Tools for JSON
"""
import json
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from typing import Callable, List


def read_jsonl(filename: str) -> List[dict]:
    with open(filename, "r") as json_file:
        return [json.loads(s) for s in json_file]


def write_jsonl(filename: str, jsonl_lines: List[dict]):
    with open(filename, "w") as f:
        for line in jsonl_lines:
            f.write(json.dumps(line) + "\n")


def excute_in_parallel(json_lines: List[dict], task_func: Callable, process_num=0) -> List[dict]:
    """Excute the same process in parallel for each line of JSONL.

    Args:
        json_lines: A JSONL list to be processed.
        task_func: A task function for each line of JSONL.
        process_num: A process number in parallel.

    Returns:
        A processed JSONL list.

    An example of the task_func:
    (Excute arbitary processing on the argument and return it.)

    def task(json_lines: List[dict]) -> List[dict]:
        new_json_lines = []
        for json_line in json_lines:
            new_json_lines.append(json_lines)
        return new_json_lines
    """
    if process_num == 0:
        process_num = multiprocessing.cpu_count()
    if len(json_lines) < process_num:
        task_num = 1
    else:
        task_num = process_num

    # Make a json_lines for each processing.
    json_lines_list = []
    lines_per_task = len(json_lines) // task_num
    for i in range(task_num):
        begin_index = lines_per_task * i
        if i < task_num - 1:  # not last case
            end_index = lines_per_task * (i + 1)
        else:  # last case
            end_index = len(json_lines)
        json_lines_list.append(json_lines[begin_index:end_index])
    futures = [0] * task_num

    # Run.
    with ProcessPoolExecutor(max_workers=process_num) as executor:
        for i in range(task_num):
            futures[i] = executor.submit(task_func, json_lines_list[i])

    # Collect the results.
    new_json_lines = []
    for future in futures:
        new_json_lines += future.result()

    return new_json_lines

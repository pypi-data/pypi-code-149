import os
import unittest
from typing import List

from hotools import json_tools


def task_func(json_lines: List[dict]) -> List[dict]:
    for json_line in json_lines:
        json_line["regions"][0]["position"]["rect"][0] += 1
    return json_lines


class JsonToolTest(unittest.TestCase):
    def test_read_jsonl_lines_num(self):
        json_lines = json_tools.read_jsonl("sample.jsonl")
        self.assertEqual(len(json_lines), 5)

    def test_read_jsonl_value(self):
        json_lines = json_tools.read_jsonl("sample.jsonl")
        self.assertEqual(json_lines[0]["image_path"], "11211314_0033_120_180_124600/000055.jpg")

    def test_write_jsonl_lines_num(self):
        json_lines = json_tools.read_jsonl("sample.jsonl")
        json_lines.append(json_lines[0])
        json_tools.write_jsonl("sample_output.jsonl", json_lines)

        new_json_lines = json_tools.read_jsonl("sample_output.jsonl")
        self.assertEqual(len(new_json_lines), 6)

    def test_write_json_value(self):
        json_lines = json_tools.read_jsonl("sample.jsonl")
        json_lines[0]["image_path"] = "sample.jpg"
        json_tools.write_jsonl("sample_output.jsonl", json_lines)

        new_json_lines = json_tools.read_jsonl("sample_output.jsonl")
        self.assertEqual(new_json_lines[0]["image_path"], "sample.jpg")

    def test_apply_parallel(self):
        json_lines = json_tools.read_jsonl("sample.jsonl")
        new_json_lines = json_tools.excute_in_parallel(json_lines, task_func, process_num=2)

        for l1, l2 in zip(json_lines, new_json_lines):
            self.assertEqual(l1["regions"][0]["position"]["rect"][0], l2["regions"][0]["position"]["rect"][0] - 1)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()

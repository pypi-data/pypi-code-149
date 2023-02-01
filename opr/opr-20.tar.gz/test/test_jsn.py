# This file is placed in the Public Domain.


"JSON tests"


import unittest



from opr.jsn import dumps, loads
from opr.obj import Object


VALIDJSON = '{"test": "bla"}'


class TestJSON(unittest.TestCase):

    def test_json(self):
        obj = Object()
        obj.test = "bla"
        res = loads(dumps(obj))
        self.assertEqual(res.test, "bla")

    def test_jsondump(self):
        obj = Object()
        obj.test = "bla"
        self.assertEqual(dumps(obj), VALIDJSON)

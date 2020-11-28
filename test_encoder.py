import unittest
import json
import encoder


class TestEncoder_Nested_Key_Value_Pairs(unittest.TestCase):
    def test_level2_text(self):
        inp1 = {"igh": "gheigh", "hieh": {"hgeih": "fheir"}, "heirg": {"eigh": "hghei"}, "eghe9": "hüghdhg"}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(
            res1,
            '{\n    "igh": "gheigh",\n    "hieh": {\n        "hgeih": "fheir"\n    },\n    "heirg": {\n        "eigh": "hghei"\n    },\n    "eghe9": "h\\u00fcghdhg"\n}',
        )
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)
    
    def test_level2_mixed(self):
        inp1 = {"igh": 245, "hieh": {"hgeih": 265.34}, "heirg": {"eigh": 223}, "eghe9": "hüghdhg"}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(
            res1,
            '{\n    "igh": 245,\n    "hieh": {\n        "hgeih": 265.34\n    },\n    "heirg": {\n        "eigh": 223\n    },\n    "eghe9": "h\\u00fcghdhg"\n}'
        )
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)


class TestEncoder_Multiple_Key_Value_Pairs(unittest.TestCase):
    def test_list_float(self):
        inp1 = {"Agerg": [1, 2, 3, 4], "Btege": 12.4}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "Agerg": [1, 2, 3, 4],\n    "Btege": 12.4\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_list_list(self):
        inp1 = {"Agerg": [1, 2, 3, 4], "Btege": [1.4, 22, 31, 434]}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "Agerg": [1, 2, 3, 4],\n    "Btege": [1.4, 22, 31, 434]\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_float_list(self):
        d = {"34.2, 45": 1.234, "23.3, 't'": [1.4, 22, 31, 434]}
        res1 = json.dumps(d, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "34.2, 45": 1.234,\n    "23.3, \'t\'": [1.4, 22, 31, 434]\n}')
        res1 = json.loads(res1)
        self.assertEqual(res1, d)


class TestEncoder_Simple_Objects(unittest.TestCase):
    def test_string(self):
        inp1 = "hgirehg"
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '"hgirehg"')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_list(self):
        inp1 = [1, 5, 32, 2, 67]
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, "[1, 5, 32, 2, 67]")
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_float1(self):
        inp1 = 452354.0001
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, "452354.0001")
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_float2(self):
        inp1 = 452354.0000
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, "452354.0")
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)


class TestEncoder_Single_Key_Value_Pair(unittest.TestCase):
    def test_list(self):
        inp1 = {"A": [1, 2, 3, 4]}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "A": [1, 2, 3, 4]\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_text(self):
        inp1 = {"BGUGUGUOrhep": "Text"}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "BGUGUGUOrhep": "Text"\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_number(self):
        inp1 = {"fwe8fhw8f": 1245}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "fwe8fhw8f": 1245\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_zeros_string(self):
        inp1 = {"FeuFFighi": "0000"}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "FeuFFighi": "0000"\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_float1(self):
        inp1 = {"hrfh Fwfiwr": 12.0000001}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "hrfh Fwfiwr": 12.0000001\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_float2(self):
        inp1 = {"hrfh Fwfiwr": 12.0000000}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "hrfh Fwfiwr": 12.0\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_float3(self):
        inp1 = {"hrfh Fwfiwr": 0.0000000}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "hrfh Fwfiwr": 0.0\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

    def test_float_str(self):
        inp1 = {"rhfgirehgi": "0.00000000001"}
        res1 = json.dumps(inp1, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(res1, '{\n    "rhfgirehgi": "0.00000000001"\n}')
        res2 = json.loads(res1)
        self.assertEqual(res2, inp1)

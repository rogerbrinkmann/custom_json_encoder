import unittest
import json
import encoder


class TestEncoder(unittest.TestCase):
    def test_dumps_simple_object(self):
        result = json.dumps("hgirehg", indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '"hgirehg"')

        result = json.dumps([1, 5, 32, 2, 67], indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '[1, 5, 32, 2, 67]')

    def test_dumps_single_key_value_pair(self):
        result = json.dumps({"A": [1, 2, 3, 4]}, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '{\n    "A": "[1, 2, 3, 4]"\n}')

        result = json.dumps({"BGUGUGUOrhep": "Text"}, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '{\n    "BGUGUGUOrhep": "Text"\n}')

        result = json.dumps({"fwe8fhw8f": 1245}, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '{\n    "fwe8fhw8f": 1245\n}')

        result = json.dumps({"FeuFFighi": "0000"}, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '{\n    "FeuFFighi": "0000"\n}')

        result = json.dumps({"hrfh Fwfiwr": 12.0000001}, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '{\n    "hrfh Fwfiwr": 12.0000001\n}')

        result = json.dumps({"rhfgirehgi": "0.00000000001"}, indent=4, cls=encoder.CustomJSONEncoder)
        self.assertEqual(result, '{\n    "rhfgirehgi": "0.00000000001"\n}')

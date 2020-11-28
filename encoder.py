from json import dumps, loads
from json.encoder import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def recursive_dict_encoder(self, dict_obj, jsonstr = "", indentationstr = ""):
        endl = "\n" if self.indent else ""

        opening = "{" + endl
        closing = endl + indentationstr + "}"

        if self.indent:
            indentationstr += " " * self.indent

        parts = []
        for key, value in dict_obj.items():
            if isinstance(value, dict):
                parts.append(JSONEncoder.encode(self, str(key)) + self.key_separator + self.recursive_dict_encoder(value, jsonstr, indentationstr))
            elif isinstance(value, list):
                parts.append(JSONEncoder.encode(self, str(key)) + self.key_separator + JSONEncoder.encode(self, str(value)))
            else:
                parts.append(JSONEncoder.encode(self, str(key)) + self.key_separator + JSONEncoder.encode(self, value))

        if self.sort_keys:
            parts.sort()

        sep = self.item_separator + endl
        output = sep.join([indentationstr + p for p in parts])

        output = opening + output + closing
        return output

    def encode(self, obj):
        if isinstance(obj, dict):
            jsonstr = self.recursive_dict_encoder(obj)
            return jsonstr
        elif isinstance(obj, list):
            return str(obj)

        return JSONEncoder.encode(self, obj)

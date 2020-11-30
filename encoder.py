from json import dumps, loads
from json.encoder import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def recursive_dict_encoder(self, dict_obj, jsonstr="", indentationstr=""):
        endl = "\n" if self.indent else ""
        opening = "{" + endl
        closing = endl + indentationstr + "}"

        if self.indent:
            indentationstr += " " * self.indent

        parts = []
        for key, value in dict_obj.items():
            if isinstance(value, dict):
                parts.append(JSONEncoder.encode(self, str(key)) + self.key_separator + self.recursive_dict_encoder(value, jsonstr, indentationstr))
            elif isinstance(value, (list, tuple)):
                parts.append(JSONEncoder.encode(self, str(key)) + self.key_separator + str(list(value)))
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
        elif isinstance(obj, (list, tuple)):
            return str(list(obj))
        return JSONEncoder.encode(self, obj)


def main():
    d = {"Abbb": [1, 2, 3, 4, 5], "BBBcccc": {"DDDDeeee": [1, 2, 3, 4, 5], "gegerg": {"gheugh": (1, 2, 3, 4)}, "DDegheig": [1, 2, 3, 4, 5]}}

    print(dumps(d, indent=4, cls=CustomJSONEncoder))
    print(dumps(d, cls=CustomJSONEncoder))
    print(dumps(d))


if __name__ == "__main__":
    main()

import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:

    with open(filename, "r") as f:
        result = []
        values = f.read().split(new_line)
        columns = values.pop(0)
        columns = columns.split(delimiter)

        for string in values:
            string = string.split(delimiter)
            dictionary = {}
            for i in range(len(columns)):
                dictionary[columns[i]] = string[i]
            result.append(dictionary)

    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

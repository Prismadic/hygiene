import json, yaml, csv
from hygiene.util.common.helpers import _csv

class DataFormatter:
    """
    A class for converting data to different formats such as JSON and CSV.

    Args:
        fmt (str): The format of the data ('json' or 'csv').
        output_path (str): The path where the CSV file will be written.
        data (str or list or tuple or dict): The data to be formatted.

    Attributes:
        fmt (str): The format of the data ('json' or 'csv').
        data (str or list or tuple or dict): The data to be formatted.
        output_path (str): The path where the CSV file will be written.

    Methods:
        format: Converts the data to the specified format.

    Raises:
        ValueError: If `fmt` is None or an unsupported data type.
        TypeError: If the YAML structure is improper and cannot be formatted.
    """

    def __init__(self, fmt=None, output_path=None, data=None):
        self.fmt = fmt
        self.data = data
        self.output_path = output_path

    def format(self):
        """
        Convert data to the specified target format.

        Returns:
            str or None: If `fmt` is 'json', the method returns a JSON string representing the formatted data.
                         If `fmt` is 'csv', the method writes the formatted data to a CSV file and returns the name of the file.

        Raises:
            ValueError: If `fmt` is None or an unsupported data type.
            TypeError: If the YAML structure is improper and cannot be formatted.
        """
        if self.fmt is None:
            raise ValueError("Formatter declared without format!")

        elif self.fmt == 'json':
            if isinstance(self.data, str):
                try:
                    yaml_obj = yaml.safe_load(self.data)
                    json_str = json.dumps(yaml_obj)
                    return json_str
                except:
                    raise TypeError("Improper yaml structure, cannot be formatted")
            elif isinstance(self.data, (list, tuple, dict)):
                # Convert Python object to JSON string
                data = json.dumps(self.data)
            else:
                raise ValueError(f'Unsupported data type "{self.data}"')
        elif self.fmt == 'csv':
            if isinstance(self.data, str):
                json_obj = json.loads(self.data)
                self.data = json_obj
            elif not isinstance(self.data, (list, tuple, dict)):
                raise ValueError(f'Unsupported data type "{self.data}"')
            # write data to CSV file
            with open(f'{self.output_path}.csv', mode='w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                _csv._write_csv_rows(self.data, writer)
                return csv_file.name
        else:
            raise ValueError(f'Unsupported data type "{self.data}"')
        return data
import json, yaml, csv
from hygiene.util.common.helpers import _csv

class DataFormatter:
    """
    A class for converting data to different formats such as YAML and CSV.

    Args:
        fmt (str): The target format for data conversion.
        output_path (str): The path where the converted data will be saved (applicable only for CSV format).
        data (str, list, tuple, dict): The data to be converted.

    Raises:
        ValueError: If the formatter is declared without a format, or if the target format is unsupported.
    """

    def __init__(self, fmt=None, output_path=None, data=None):
        self.fmt = fmt
        self.output_path = output_path
        self.data = data

    def format(self):
        """
        Convert data to the specified target format.

        Returns:
            str: If the target format is 'yaml' or 'yml', returns a YAML string representing the converted data.
            str: If the target format is 'csv', returns the name of the CSV file where the data is saved.

        Raises:
            ValueError: If the formatter is declared without a format, or if the target format is unsupported.
        """
        if self.fmt is None:
            raise ValueError("Formatter declared without format!")

        elif self.fmt in ['yaml', 'yml']:
            if isinstance(self.data, str):
                json_obj = json.loads(self.data)
                yaml_str = yaml.dump(json_obj, default_flow_style=False)
                return yaml_str
            elif isinstance(self.data, (list, tuple, dict)):
                # Convert Python object to YAML string
                data = yaml.dump(self.data, default_flow_style=False)
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
            raise ValueError(f'Unsupported target format "{self.fmt}"')
    
        return data
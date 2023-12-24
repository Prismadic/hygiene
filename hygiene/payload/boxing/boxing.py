from hygiene.util.formatters.single import json, yaml
from hygiene.util.builders import csv
import os

class Payload:
    """
    The `Payload` class is responsible for formatting and delivering data based on the specified format.
    It supports CSV and JSON formats and can handle data in the form of dictionaries, lists, and strings.
    """

    def __init__(self, data=None, path=None, fmt=None):
        """
        Initializes the `Payload` object with the provided data, output path, and format.

        :param data: The data to be formatted and delivered.
        :param path: The path where the formatted data will be saved (only applicable for CSV format).
        :param fmt: The format in which the data should be formatted (e.g., 'csv' or 'json').
        """
        self.data = data
        self.output_path = path
        self.fmt = fmt

    def deliver(self):
        """
        Formats and delivers the data based on the specified format.

        :return: The formatted data.
        """
        if self.fmt == 'csv':
            form = csv.DataFormatter(fmt=self.fmt, data=self.data, output_path=os.path.abspath(self.output_path))
            with open(form.format(), 'r') as f:
                return f.readlines()
        elif isinstance(self.data, (dict, list)):
            form = json.DataFormatter(fmt=self.fmt, data=self.data)
            return form.format()
        elif isinstance(self.data, str):
            return self.data
            try:
                form = yaml.DataFormatter(fmt=self.fmt, data=dict(self.data))
            except:
                form = json.DataFormatter(fmt=self.fmt, data=self.data)
            return form.format()
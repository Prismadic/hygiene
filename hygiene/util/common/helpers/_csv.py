def _write_csv_rows(data, writer):
    """
    Write data to a CSV file.

    Args:
        data (any): The data to be written to the CSV file. It can be a list of dictionaries, a single dictionary, or an integer value.
        writer (csv.writer): The CSV writer object used to write the data to the file.

    Raises:
        ValueError: If the data type is not supported.

    Example Usage:

        # Create a CSV file
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            # Write a list of dictionaries to the CSV file
            data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]
            _write_csv_rows(data, writer)

            # Write a single dictionary to the CSV file
            data = {'name': 'Alice', 'age': 35}
            _write_csv_rows(data, writer)

            # Write an integer value to the CSV file
            data = 42
            _write_csv_rows(data, writer)
    """
    if isinstance(data, list):
        if isinstance(data[0], dict):
            _write_csv_rows(data[0], writer)
    elif isinstance(data, dict):
        writer.writerow(data.keys())
        writer.writerow(list(data.values()))
    elif isinstance(data, int):
        writer.writerow([data])
    else:
        raise ValueError(f'Unsupported data type "{data}"')

import csv

class Sequence:
    """
    Initialize the Sequence object with a list of column names.

    Args:
        columns (list): A list of column names.

    Raises:
        ValueError: If the builder was declared without columns.

    Returns:
        None
    """
    def __init__(self, columns):
        self.columns = columns

    def build(self, data, out):
        """
        Process the data from a CSV file and add a new column with concatenated values.
    
        Args:
            data (str): The path to the CSV file containing the data to be processed.
            out (str): The name of the output file to which the modified rows will be written.
    
        Raises:
            ValueError: If the builder was declared without columns to collate.
    
        Returns:
            None
    
        Example Usage:
            sequence = Sequence(['name', 'age', 'city'])
            sequence.build('input.csv', 'output')
        """
        if self.columns is None:
            raise ValueError("Builder declared without columns to collate!")
    
        reader = csv.DictReader(data)

        # Create a new column with the concatenated values
        for row in reader:
            sequenced = " ###".join([f"{column}: {row[column]}" for column in self.columns])
            row['sequence'] = sequenced

            # Output the modified row to a new CSV file
            with open(f'{out}.csv', 'a', newline='') as f:
                writer = csv.DictWriter(out, fieldnames=reader.fieldnames + ['sequence'])
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow(row)

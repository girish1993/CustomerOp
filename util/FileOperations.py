import pandas as pd
import os
class FileOperations:

    def __init__(self, path_to_file):
        """
        Constructor for the File Operations class
        Parameters
        ----------
        path_to_file :
        """
        self.path_to_file = path_to_file
        self.file_content = None

    def is_file_exists(self):
        """
        Method to check if the csv file exists in the provided path
        Returns
        -------
        Boolean : True or False on whether file exists or not
        """
        if os.path.isfile(self.path_to_file):
            return True
        else:
            return False

    def read_file_content_and_return_records(self):
        """
        Method to read the content of the file
        Returns
        -------
        A list of records in the data frame
        """
        if self.is_file_exists():
            self.file_content = pd.read_csv(self.path_to_file)
            return list(self.file_content.to_records(index=False))
        else:
            raise FileNotFoundError("The file 'customer_information.csv' is not found under /data")



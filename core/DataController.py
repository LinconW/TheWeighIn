import pandas as pd

class DataController:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        
    def read_column(self, column_name):
        return self.df[column_name].tolist()
    
    def add_row(self, row_dict):
        self.df = pd.concat([self.df, pd.DataFrame([row_dict])], ignore_index=True)
        self.save()

    def has_column(self, col):
        return col in self.df.columns

    def save(self):
        self.df.to_csv(self.file_path, index=False)
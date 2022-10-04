import pandas as pd
from numpy import array
import os.path


class Data:

    def __init__(self, data: str) -> None:
        if os.path.exists(data.strip('\"')):
            self.data = data.strip('\"')
        else:
            raise FileExistsError(f"Файл {data} не найден")
        self.sheets = self.X = self.Xnames = self.Y = self.df = self.Yname = None

    def getdftoarrayxlsx(self, sheetwithx: int = 0, sheetwithy: int = 1):
        df = pd.read_excel(self.data, sheet_name=None)
        self.sheets = list(df.keys())
        self.Xnames = df[self.sheets[sheetwithx]].columns
        self.X = array(df[self.sheets[sheetwithx]].replace(',', '.'))
        if len(self.sheets) == 2:
            self.Y = array(df[self.sheets[sheetwithy]].replace(',', '.')).flatten()
            self.Yname = list(df[self.sheets[sheetwithy]].columns)[0]
        elif len(self.sheets) == 1:
            pass
        else:
            raise KeyError
        return self

    def getdfxlsx(self, sheetwithx: int = 0, sheetwithy: int = 1):
        self.df = pd.read_excel(self.data, sheet_name=None)
        self.sheets = list(self.df.keys())
        self.Xnames = self.df[self.sheets[sheetwithx]].columns
        if len(self.sheets) == 2:
            self.Y = array(self.df[self.sheets[sheetwithy]].replace(',', '.')).flatten()
            self.Yname = list(self.df[self.sheets[sheetwithy]].columns)[0]
        elif len(self.sheets) == 1:
            pass
        else:
            raise KeyError
        return self

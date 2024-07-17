import os
import pandas as pd



DEFAULT_PATH: str = os.path.expanduser('~\\Desktop')



class Excel:


    def __init__(self, headers: list[str]):
        self._dataframe: pd.DataFrame | None = None
        self._headers: list[str] = headers
        self._data: list[list[str]] = []
        self._size: int = 0


    def load(self, data: list[dict], parsers: dict | None = None) -> None:
        row: list[str] = []

        for item in data:
            for header in self._headers:
                if header in parsers:
                    row.append(parsers[header](item[header]))
                else:
                    row.append(item[header])

            self._data.append(row)
            self._size += 1

            row = []


    def build(self) -> None:
        self._dataframe = pd.DataFrame(
            data=self._data,
            columns=self._headers
        )


    def save(self, sheet: str) -> str:
        filename: str = '{}\\{}.xlsx'.format(DEFAULT_PATH, sheet)

        self._dataframe.to_excel(
            excel_writer=filename,
            sheet_name=sheet,
            index=False
        )

        return '{} Linhas salvas no arquivo "{}"'.format(self._size, filename)

import re
import types
from typing import Tuple


def hasmethod(cls, method_name: str) -> bool:
    return hasattr(cls, method_name) and callable(getattr(cls, method_name))


class ImportAdapterBase:
    """
        returns a tuple list containing three indices: the first is the line index, the second is the method name,
        and the third is the expected return type
    """
    list_methods = []

    def __init__(self, row: Tuple[str]) -> None:
        self._row = row
        self._clean_methods()

    def get_string_value(self, index: int) -> str:
        return str(self._row[index])

    def get_int_value(self, index: int) -> int:
        number, *_ = re.findall(r'-?\d+', self._row[index])
        return int(number)

    def _clean_methods(self) -> None:
        for index, method, expected_return in self.list_methods:
            if not hasattr(self, f'get_{method}'):
                if expected_return is str:
                    setattr(self, f'get_{method}', types.MethodType(self.get_string_value, index))
                elif expected_return is int:
                    setattr(self, f'get_{method}', types.MethodType(self.get_int_value, index))

    def get_adapted_line(self) -> dict:
        data = {}
        for index, method, expected_return in self.list_methods:
            if hasmethod(self, f'get_{method}'):
                data.update({method: getattr(self, f'get_{method}')()})
        return data

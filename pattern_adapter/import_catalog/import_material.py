from typing import Tuple
from pattern_adapter.base.adapter import ImportAdapterBase
from pattern_adapter.base.spreadsheet_catalog import SpreadsheetCatalogBase


class ImportMaterialAdapter(ImportAdapterBase):
    list_methods = [
        (0, 'type', str),
        (1, 'group', int),
        (2, 'group_description', str),
        (3, 'class', int),
        (4, 'class_description', str),
        (5, 'pdm_code', int),
        (6, 'pdm_description', str),
        (7, 'item_code', int),
        (8, 'item_description', str),
        (9, 'status', str),
        (10, 'sustainable_item', str)
    ]


class ImportSpreadsheetMaterialCatalog(SpreadsheetCatalogBase):
    spreadsheet = 'catmat112023.xlsx'

    def get_class_import(self, line: Tuple[str]) -> dict:
        return ImportMaterialAdapter(line).get_adapted_line()

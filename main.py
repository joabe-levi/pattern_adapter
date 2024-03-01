from pattern_adapter.import_catalog.import_material import ImportSpreadsheetMaterialCatalog
from pattern_adapter.import_catalog.import_service import ImportSpreadsheetServiceCatalog


def main():
    catalog_material_importer = ImportSpreadsheetMaterialCatalog().get_list_from_catalog()
    catalog_service_importer = ImportSpreadsheetServiceCatalog().get_list_from_catalog()

    print('Material Catalog: ')
    print(catalog_material_importer)

    print('Service Catalog: ')
    print(catalog_service_importer)


if __name__ == "__main__":
    main()

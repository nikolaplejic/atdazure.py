import azurecfg
from azure.storage import TableService, Entity

table_service = TableService(
    account_name=azurecfg.table_storage['account_name'],
    account_key=azurecfg.table_storage['account_key']
)

table_service.create_table('atd')

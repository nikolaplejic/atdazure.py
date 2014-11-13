import azurecfg
from azure.servicebus import ServiceBusService, Message, Queue

bus_service = ServiceBusService(
        service_namespace='atdblasphemy',
        shared_access_key_name=azurecfg.servicebus['name'],
        shared_access_key_value=azurecfg.servicebus['key'])

bus_service.create_queue('atd')

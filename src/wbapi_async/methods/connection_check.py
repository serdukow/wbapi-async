from ..types.connection_check import ConnectionCheck as ConnectionCheckType
from .base import WbMethod


class ConnectionCheck(WbMethod):
    __return__ = ConnectionCheckType
    __api__ = "common-api"
    __method__ = "ping"

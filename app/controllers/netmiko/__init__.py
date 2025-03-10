from .junos.set_static_route import set_static_route
from .junos.set_interface_unit import set_interface_unit
from .junos.get_interface_ae0_summary import get_interface_ae0_summary
from .junos.get_interface_configuration import get_interface_configuration


__all__ = [
    'set_static_route',
    'set_interface_unit',
    'get_interface_ae0_summary',
    'get_interface_configuration',
]

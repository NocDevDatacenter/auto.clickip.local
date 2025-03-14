from .network_form import NetworkForm
from .auth_form import LoginForm, RegisterForm
from .set_static_route_form import StaticRouteForm
from .downstream_fec_form import Downstream_fec_form
from .bgp_manager_session_form import BgpManagerSessionForm
from .set_access_address_assignment import AddressAssignmentForm


__all__ = [
    'LoginForm',
    'NetworkForm',
    'RegisterForm',
    'StaticRouteForm',
    'Downstream_fec_form',
    'BgpManagerSessionForm',
    'AddressAssignmentForm',
]

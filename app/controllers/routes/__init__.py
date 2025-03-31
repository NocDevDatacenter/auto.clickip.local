from flask import Flask
from .auth import auth_bp
from .junos.interface_unit import int_unit_bp
from .junos.interface_dhcp import int_dhcp_bp
from .dmos.downstream_fec import downstream_fec_bp
from .junos.get_interface_ae0_summary import int_summary_bp
from .junos.get_interface_ae0_config import int_conf_bp
from .junos.bgp_manager import bgp_manager_bp
from .junos.interface_static_router import int_static_route_bp


def register_blueprints(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(int_conf_bp, url_prefix='/network')
    app.register_blueprint(int_dhcp_bp, url_prefix='/network')
    app.register_blueprint(int_unit_bp, url_prefix='/network')
    app.register_blueprint(int_summary_bp, url_prefix='/network')
    app.register_blueprint(downstream_fec_bp, url_prefix='/network')
    app.register_blueprint(int_static_route_bp, url_prefix='/network')
    app.register_blueprint(bgp_manager_bp, url_prefix='/network')

from flask import Flask
from .auth_routes.auth import auth_bp
from .network.junos_routes.interface_unit import int_unit_bp
from .network.junos_routes.interface_dhcp import int_dhcp_bp
from .network.dmos_routes.downstream_fec import downstream_fec_bp
from .network.junos_routes.interface_summary import int_summary_bp
from .network.junos_routes.interface_configuration import int_conf_bp
from .network.junos_routes.bgp_manager_session import bgp_manager_session_bp
from .network.junos_routes.interface_static_router import int_static_route_bp


def register_blueprints(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(int_conf_bp, url_prefix='/network')
    app.register_blueprint(int_dhcp_bp, url_prefix='/network')
    app.register_blueprint(int_unit_bp, url_prefix='/network')
    app.register_blueprint(int_summary_bp, url_prefix='/network')
    app.register_blueprint(downstream_fec_bp, url_prefix='/network')
    app.register_blueprint(int_static_route_bp, url_prefix='/network')
    app.register_blueprint(bgp_manager_session_bp, url_prefix='/network')

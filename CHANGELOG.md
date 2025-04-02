## v0.13.0 (2025-04-02)

### Feat

- **app/controllers/admin/admin.py**: add new feature, fileadmin like uploads in admin painel
- **app/templates/includes/sidebar.html**: add a button to close and open sidebar

### Fix

- **app/controllers/admin/admin.py**: add logout button in top header flask_admin
- **app/templates/admin/index.html**: refactored /admin/index.html
- **app/controllers/admin/admin.py**: add new menu link, logout
- **app/models/__init__.py**: add is_admin = db.Column(db.Boolean, default=False)
- **app/templates/admin/index.html**: del <li><a href="/admin/users/">Users</a></li>
- **app/controllers/routes/auth/__init__.py**: redirect return to interface_summary
- **app/templates/vendors/dmos/downstream_fec.html**: add endpoint in action form
- **app/templates/includes/sidebar.html**: hidden menu items
- adjusted get config to bs5
- **app/controllers/forms/get_interface_ae0_summary.py**: delete enpty spaces
- **livereloader.py**: upt livereloader.py
- **base.html**: remove class container of the tag main

### Refactor

- ****/*/downstream_fec.***: refact downstream_fec

## v0.12.0 (2025-03-27)

### Feat

- **netmiko/junos/bgp_manager.py**: done, finally finished function to deactivate and activate neighbor in bgp protocol

### Fix

- **bgp_manager.html**: script upt to refresh data with ajax
- **bgp_manager.py**: finally configured to work with bgp manager
- **footer.html**: not implemented yet
- **main.js**: its not necessary
- **setup.py**: upt version to 0.1.0

## v0.11.0 (2025-03-27)

### Feat

- **/app/config.py**: env_path to ensure load env

### Fix

- change bgp_manager_session name to bgp_manager
- del bgp_manager.py of the __init__.py
- upt form bgp_manager
- upt bgp_manager.html
- changed name bgp_manager_session.xyz to bgp_manager.xyz

## v0.1.0 (2025-03-25)

## v0.10.1 (2025-03-25)

### Fix

- upt flash_messages.html
- del templates/vendors/junos/get_interface_ae0_summary.html tag </pre>
- upt description forms/get_interface_ae0_summary.py

## v0.10.0 (2025-03-25)

### Fix

- hulk smash
- upt .env.example
- upt app/config.py
- add new folder in routes
- caquinha :poop
- upt sidebar.html

## v0.9.0 (2025-03-25)

### Feat

- renamed app/controllers/blueprints to routes

### Fix

- rename /interface_summary.py to /get_interface_ae0_summary.py
- remove comments in app/controllers/netmiko/junos/get_interface_ae0_summary.py

## v0.7.1 (2025-03-25)

### Feat

- add dropdown in end of sidebar
- added commitizen like as requirements
- add pyproject.toml
- add setup.py
- add sidebar in site
- livereloader add new file, styles.css
- new page register.html, working on it
- new page, register.html
- add new feature, auth/register
- add livereloader
- new feature bgp manager session, not finished yet
- Add BGP Manager Session
- add a simple list in admin/index.html
- add new feature, add new table in module
- add dotenv to requirements.txt
- add no_downstream_fec in dmos routes
- add no_downstream_fec.py
- add downstream_fecc form and routes
- add new feature, downstream_fec on olt datacom
- add new page set_access_address_assignment (work on it)
- add new feat create admin in database
- add sandbox.* in gitignore
- add some scripts with netconf
- add new model Switches
- add ncclient package to requirements.txt
- Add static route page
- add static route page
- app new netmiko file set_static_route.py
- add new route to set static route
- add Flask-Migrate==4.0.7 in requirements.txt
- add migrations in gitignore
- add migrate in project
- add comment super() in get_interface_configuration and set_interface_unit
- add comments in layout, login and get_interface_summary
- add livereload to the app
- add simple eye to interface summary
- enable fontawesome and jquery
- att javascript in project with jquery
- enable css in project and add style.css
- add fontawesome to layout
- add eye icon to show/hide password
- add cryptograpy in project
- add management admin
- add new file in blueprints admin
- add file config.py in project app
- add flask_admin in requirements
- add app/templates/admin/index.html to flask_admin
- flask_admin
- add new function create_admin(app)
- add new functions login_manager
- add login_user(user, remember=True)
- add new file package controllers __init__.py
- list users
- new route for list users
- add new page_list_user
- add new page_list_user
- add new right menu in layout
- add new page in user folder, page_list_user
- add func cad new circuit in juniper router.
- create test files
- add NumberRange(min=1, max=4096)
- new page set_interface_unit
- add flake8 in Makefile
- add docker-ls in Makefile.
- add host 0.0.0.0 in run.py
- add clear .pytest_cache folder in Makefile.
- new page config_static_router
- new page config interface unit
- new func config_interface_unit
- new page, config interface
- add clear cache in Makefile
- add new file Makefile with flask run

### Fix

- upt app/templates/includes/sidebar.html with username in dropdown
- upt livereloader.py
- upt app/config.py
- upt app/templates/base.html
- upt livereloader
- web_reloader is default false
- remove delay in livereloader
- upt changelog.md
- add more time to livereloader
- **changed-icon-of-the-i-tag**: sidebar.html
- renamed templates/network to templates/vendors
- add container class in main
- add new sidebar in site
- upt livereloader
- migrated WEB_RELOADER to config.py
- upt make run and clean functions
- upt livereloader with delay=0.5 in server.watch
- upt .gitignore with .vscode/*
- upt login.html and register.html to bootstrap5
- migrate from bootstrap 4 to 5
- update database name
- upt app/controllers/forms/auth_form.py
- del placebo inputs, username and password in bgp_manager_session
- upt app/templates/admin/index.html
- changed default action to deactivate neighbor bgp
- changed database name to nexus.database
- refactored login.html
- del flash message in register.html
- refactored login.html
- del flash message in register.html
- update register.html
- change blueprint auth to auth_bp
- update .env.example
- re-order login.py above register.py
- update register.html
- update livereloader.py, requirements.txt and head.html to work with scss
- updated livereloader
- changed name of login_form to auth_form
- fixed formating to better redability
- trivial commit
- reorganized templates folders and added new ones files
- updated text center int the front end
- add __init__.py in blueprints/network
- renamed auto_routes to auth
- updated of the folders named routes to blueprints
- updated names of the blueprints and auth folders
- add load_dotenv to deactivate_bgp_v6_ebt_1G.py
- fix reference in get_interface_ae0_summary.py
- changed get_interface_configuration to get_interface_ae0_config
- changed blueprints to blueprints_routes
- change name functions get_interface_summary to get_interface_ae0_summary
- add a new page in list in admin/index.html
- redirect to admin page after login
- enable autocomple in form fields
- little change in flash message in login route
- little fix layout.html
- add import os to all file and fix env variables
- little fix in makefile
- add more ports to downstream_fec_form.py
- translate dmos error message to english
- add missing import in dmos/__init__.py
- just a tweak to improve the readability of the code.
- del print in create_admin.py
- trivial commit
- trivial commit, just delete flakes8 errors and warnings: E501
- little fix in flash message
- trivial commit
- fix imports in network blueprints
- fix identation in set_static_route_form.py
- changed files to reflect new junos_routes directory structure
- add ensure_admin as function in create_admin
- clean hardcoded
- create_admin to flask_admin it's the same purpose
- Device to Routers
- changed background off application to #F4F4F4F
- sandbox.py -> app/sandbox.py
- chat route to junos folder in network blueprints
- Corrected import statement in netmiko __init__.py
- renamed router folder to junos
- move files python to junos folder.
- move python files to junos folder
- remove rm -rf .venv from Makefile
- sort by hostname in model switches
- changed the name of the networks directory to netmikok
- del trivial imports
- set static route configuration
- set_static_route.py: fix the bug that the static route is not set correctly
- sort imports in networks/__init__.py
- add form folder and move forms to it
- sort imports in app/__init__.py
- add set interfaces ae0 unit {unit} in set_interface_unit.html
- can_delete = false in admin/__init__.py
- fix typo in run.py
- delete user folder
- migrate db.create_all() to __init__.py
- turned off autocomplete on input fields
- updated limite of characters to 12
- deactivate username and password of network form
- added limit to password in frontend to 24 characters
- changed redirect to get_interface_summary
- changed to current_user.username and current_user.password
- add validation lengh to form networkform
- diable livereload in app __init__.py
- att text in page login and summary page
- just formatting to better view
- del head in head.html and add in layout.html
- del padding login.html
- add a simple paddint-top to center eye icon
- fix toggle action show and hide password
- fix action in login page and get_interface_summary page
- redirect home to login page
- formatting to better view the page
- login page
- fix the style of the login page
- remove font-family arial from project
- foo
- formatting to better view and update variables names.
- bla
- foo
- enable javascript
- foo
- lm.refresh_view = "auth.login"
- lm.login_view = 'auth.page_login' to 'auth.login'
- not AnonymousUserMixin: in summary
- fernet
- better view
- del form devices
- del register_form
- del button register
- foo
- foo
- foo
- add @loguin_required in network_devices CRUD
- rename class Network_Form to Form_Network to comprehension
- add more space to better view.
- update tablenames for batter comprehension
- app/models/model.py -> app/models/__init__.py
- add create_admin in run.py
- just little fix in admin = Admin()
- bla
- rename login_manager to lm
- rename login_manager to lm
- clear spaces of the run.py
- add login_required
- add required and redirect to network.interface_summary
- update Form_Devices from 10 to 30
- changed message from loging_message to \ Please log in to access this page
- delete build from Makefile
- changes .virt do venv in Makefile.
- add new line in set_interface_unit for view static route
- clear white space near {{output}}
- changed name db aplication to app.db
- removed netmiko file and adjust functions.
- removed netmiko file and fragmented in others
- remove get_ prefix of the url_for
- del dependencie remove venv of the Makefile
- fix identation of page_list_user
- just trivial fix for better view of the right menu
- att home page
- add new menu context
- change router to route
- add new command in Makefile:flake8
- renamed directory to route insted router
- just delele a trivial comment, page works!
- del table users in page_register_user
- del breadcrumb in page home.html
- just add  # noqa: E501 in line 56
- delete redirect, url_for from import
- formatting to better code view
- formatting to according flake8
- change name make test to make flake
- del make docker-ls
- just formatting for better view of code forms
- reverse bandwidth with ipv4_gw
- formatting to according flake8
- del func validate_ipv6, formatting to according flak8
- resolved func validate_ipv6
- resolved conflicts in merge
- formatting to according with flake8
- fix indentation for better view
- placeholder="ipv6.48" to ipv6_48
- formatting to according flake8
- del line host='0.0.0.0' in run.py
- change image in dockerfile for python:3.11-alpine
- add flake8 in requirements
- formatting according to flake8
- update makefile, hide output
- Update ci.yml
- update .gitignore
- update makefile
- rename to requirements.txt
- formatting according to flake8
- new func, create_app()
- import create_app() in run.py
- formatting according to flake8
- formattng according to flake8
- update ci.yml with requirements.md
- add gunicorn and pytest in requirements.
- Update ci.yml
- Rename dependencies.md to requirements
- Update ci.yml
- Update ci.yml
- formatting according to flake8
- formatting according to flake8
- nomenclatura do param {{tab.id}}...
- {{ tab.id }}/remove to /del
- clear no arquivo de rotas principais
- url e comentários
- ajuste nas url
- delete value option selector in summary

### Refactor

- improve blueprint structure and readability
- add head.html template
- change the layout of the web page
- get_interface_summary page
- refactor .gitignore

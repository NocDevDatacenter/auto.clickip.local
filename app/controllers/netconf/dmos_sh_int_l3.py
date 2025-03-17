import os
from rich import print
from ncclient import manager
from dotenv import load_dotenv
from xml.dom.minidom import parseString

load_dotenv()

router = {
    'host': '100.127.0.254',
    'port': 830,
    'username': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD'),
    'hostkey_verify': False,
}


def connect_to_router():
    filter = '''
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <config xmlns="urn:dmos">
            <interface>
                <l3 xmlns="urn:dmos:dmos-ip-application"/>
            </interface>
        </config>
    </filter>
    '''
    try:
        with manager.connect(**router) as m:
            output = m.get_config('running', filter=filter).data_xml
            xml_output = parseString(output).toprettyxml(indent=(' ' * 2))
            print(xml_output)
    except Exception as e:
        print(f'Erro ao conectar: {e}')


connect_to_router()

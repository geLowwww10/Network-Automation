import json
from webexteamssdk import WebexTeamsAPI
from ncclient import manager
import xml.etree.ElementTree as E

def load_config():
    with open('config/config.json') as config_file:
        return json.load(config_file)

def change_interface_description(router_ip, username, password, interface_name, new_description):
    # Establish NETCONF connection
    with manager.connect(
        host=router_ip,
        port=830,
        username=username,
        password=password,
        hostkey_verify=False
    ) as mgr:
        # Create XML payload to modify the description (based on YANG model)
        config_xml = f"""
        <config>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{interface_name}</name>
                    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
                    <description>{new_description}</description>
                </interface>
            </interfaces>
        </config>
        """
        # Send the configuration update
        mgr.edit_config(target='running', config=config_xml)
        # Verify the new running configuration
        new_running_config = mgr.get_config(source='running').data_xml
        return new_running_config

def send_webex_notification(webex_token, room_id, message):
    api = WebexTeamsAPI(access_token=webex_token)
    # Split the message into smaller parts if it exceeds the length limit
    max_length = 7439
    messages = [message[i:i+max_length] for i in range(0, len(message), max_length)]
    for msg in messages:
        api.messages.create(room_id, text=msg)

def main():
    config = load_config()
    # Change the interface description using NETCONF
    new_config = change_interface_description(
        config['router_ip'],
        config['username'],
        config['password'],
        config['interface_name'],
        config['description']
    )
    # Send WebEx notification about the update
    send_webex_notification(config['webex_token'], config['room_id'], new_config)

if __name__ == "__main__":
    main()
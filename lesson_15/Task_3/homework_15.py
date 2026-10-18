import xml.etree.ElementTree as ET
from xml_log import log_xml
tree = ET.parse('groups.xml')
root = tree.getroot()

def find_incoming(group_number):
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(group_number):
            timingExbytes = group.find('timingExbytes')
            if timingExbytes is not None:
                incoming = timingExbytes.find('incoming')
                if incoming is not None:
                    return incoming.text
            return None
    return None

group_number = 6
result = find_incoming(group_number)

if result is not None:
    log_xml(f'Значення incoming для группи {group_number}: {result}')
else:
    log_xml(f'Группа або елемент incoming у группi {group_number} не знайдено')
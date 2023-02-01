import xml.etree.ElementTree as ET
import json

def xml_to_json(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = {}

    for elem in root:
        data[elem.tag] = elem.text

    with open(json_file, 'w') as f:
        json.dump(data, f)

xml_to_json('input.xml', 'output.json')

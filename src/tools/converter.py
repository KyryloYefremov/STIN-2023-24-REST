import xmltodict
import json


def xml_to_json(xml_string):
    return json.dumps(xmltodict.parse(xml_string), indent=4)


def json_to_xml(json_string):
    return xmltodict.unparse(json.loads(json_string), pretty=True)

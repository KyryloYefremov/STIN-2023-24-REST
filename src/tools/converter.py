import xmltodict


def json_to_xml(_json: dict) -> str:
    """
    Converts a json to xml
    :param _json: json to be converted
    :return: xml string
    """
    return xmltodict.unparse(_json, pretty=True)

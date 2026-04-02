import xml.etree.ElementTree as ET
from collections import namedtuple

def xml_to_dict(element):
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if not child_data and child.attrib and 'value' in child.attrib:
            child_data = child.attrib['value']
        elif not child_data and child.attrib:
            child_data = dict(child.attrib)
            
        result[child.tag] = child_data
    
    if not result and element.attrib:
        if 'value' in element.attrib and len(element.attrib) == 1:
            return element.attrib['value']
        return dict(element.attrib)
    
    if not result and element.text:
        return element.text.strip()
        
    return result

def parse_body(text):
    try:
        root = ET.fromstring(text)
        parsed_data = {}
        for child in root:
            if child.tag in ('output', 'output1', 'output2', 'output3', 'data'):
                if child.tag not in parsed_data:
                    parsed_data[child.tag] = []
                
                results = child.findall('.//result') or child.findall('.//row')
                if results:
                    for res_node in results:
                        parsed_data[child.tag].append(xml_to_dict(res_node))
                else:
                    node_data = xml_to_dict(child)
                    if node_data:
                        parsed_data[child.tag].append(node_data)
            else:
                parsed_data[child.tag] = child.text.strip() if child.text else xml_to_dict(child)
        
        return parsed_data
    except Exception as e:
        return str(e)

xml_text = """<vector result="1">
<header></header>
<xdaresult result="1" beforeEJBCall="1775052683900" afterEJBCall="1775052683902"/>
<data vectorkey="0" type="Document">
<result>
<ISSUCO_CUSTNO value="29998"/>
<KOR_SECN_NM value="SK해운 61"/>
</result>
</data>
</vector>"""

print(parse_body(xml_text))

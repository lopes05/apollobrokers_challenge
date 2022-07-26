from django.core.files.base import ContentFile
import xml.etree.ElementTree as ET

class InvalidXMLError(Exception):
    pass

class XMLConverterToDict:

    def __init__(self, xml_file):
        if isinstance(xml_file, str):
            xml_file = ContentFile(xml_file)
        self.xml_file = xml_file
        try:
            self.tree = ET.parse(xml_file)
        except ET.ParseError:
            raise InvalidXMLError("File is not a XML or is badly formed.")
    
    def to_dict(self):
        result_dict = {}
        root = self.tree.getroot()
        result_dict[root.tag] = self.get_root_children(root)
        result_dict[root.tag] = '' if not result_dict[root.tag] else result_dict[root.tag]
        return result_dict
    
    def get_root_children(self, root):
        result_list = []
        for child in root:
            if child.getchildren():
                result_list.append(
                    {
                        child.tag: self.get_root_children(child)
                    }
                )
            else:
                result_list.append({
                    child.tag: child.text
                })
        return result_list

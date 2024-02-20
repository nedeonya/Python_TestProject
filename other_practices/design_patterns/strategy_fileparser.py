from abc import ABC, abstractmethod
from typing import List, Dict, Any
import xml.etree.ElementTree as ET
import json
import csv


class FileParser(ABC):
    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass


class CSVParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        result = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                result.append(dict(row))
        return result


class JSONParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data


class XMLParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        result = []
        tree = ET.parse(file_path)
        root = tree.getroot()
        for element in root:
            item = {}
            for attribute in element.attrib:
                item[attribute] = element.attrib[attribute]
            result.append(item)
        return result


class FileReader:

    def __init__(self, file_parser: FileParser):
        self.file_reader = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        return self.file_reader.parse_file(file_path)


#Testing
if __name__ == "__main__":
    reader = FileReader(CSVParser())

    data = reader.read_file("files/contacts.csv")
    print(data)

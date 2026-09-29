import csv
import json
import logging
import xml.etree.ElementTree as ET

import yaml


def parse_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        logging.info("PARSE_JSON_SUCCESS")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logging.error("PARSE_JSON_ERROR: %s", error)
        return []


def parse_yaml(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        logging.info("PARSE_YAML_SUCCESS")
        return data
    except (FileNotFoundError, yaml.YAMLError) as error:
        logging.error("PARSE_YAML_ERROR: %s", error)
        return []


def parse_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = []
        for vlan in root.findall("vlan"):
            data.append({
                "id": vlan.findtext("id", default=""),
                "name": vlan.findtext("name", default=""),
            })
        logging.info("PARSE_XML_SUCCESS")
        return data
    except (FileNotFoundError, ET.ParseError) as error:
        logging.error("PARSE_XML_ERROR: %s", error)
        return []


def parse_csv(filename):
    try:
        with open(filename, "r", encoding="utf-8", newline="") as file:
            data = list(csv.DictReader(file))
        logging.info("PARSE_CSV_SUCCESS")
        return data
    except (FileNotFoundError, csv.Error) as error:
        logging.error("PARSE_CSV_ERROR: %s", error)
        return []
import requests
import xml.etree.ElementTree as ET #Warning The xml.etree.ElementTree module is not secure against maliciously constructed data. If you need to parse untrusted or unauthenticated data see XML vulnerabilities.
from urllib.parse import urlparse, parse_qs

def collect_url(url, xml):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the text content from the response
            xml_content = response.text
            print("Successfully fetched text content from "+ url)
            # Save the XML content to a local file
            with open(xml, 'w') as file:
                file.write(xml_content)
        else:
            print(f"Failed to fetch the content. HTTP Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def number_of_urls(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        x = 0
        for child in root:
            x = x+1
        return x
    except Exception as e:
        print(f"Failed to parse {xml_file}: {e}")
        return []

def get_url_lines(xml_file, x):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        #print(root[x][0].text)
        return root[x][0].text
    except Exception as e:
        print(f"Failed to parse {xml_file}: {e}")
        return []

def get_url_path(input_url):
    # Parse the URL into components
    url_parts = urlparse(input_url)
    #print(url_parts.path)
    return url_parts.path

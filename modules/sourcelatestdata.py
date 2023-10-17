# __author__ = 'Anjan Kumar Devara"

import requests
import logging
import allure  # Import the Allure library

# Configure the logger
logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def get_data_from_url(methodname, url, headers, payload={}):
    try:
        logging.info(f"Calling {methodname} for URL: {url}")
        # Use Allure to mark a step
        with allure.step(f"Calling {methodname} for URL: {url}"):
            if methodname == 'GET':
                response = requests.get(url, headers=headers)
            elif methodname == 'PUT':
                response = requests.put(url, headers=headers, data=payload)
            elif methodname == 'POST':
                response = requests.post(url, headers=headers, data=payload)
            elif methodname == 'DELETE':
                response = requests.delete(url, headers=headers, data=payload)
            else:
                raise ValueError(f"Invalid method name: {methodname}")

        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log the error using Allure
        allure.attach(f"Request to URL failed: {str(e)}", name="Error", attachment_type=allure.attachment_type.TEXT)
        logging.error(f"Request to URL failed: {str(e)}")
        return None
    except ValueError as e:
        # Log the error using Allure
        allure.attach(f"Invalid method name: {str(e)}", name="Error", attachment_type=allure.attachment_type.TEXT)
        logging.error(f"Invalid method name: {str(e)}")
        return None

def find_source_id(data, source_id_to_find):
    try:
        for item in data.get('data', []):
            source_id = item.get('SourceId')
            if source_id == source_id_to_find:
                return source_id
    except (KeyError, AttributeError) as e:
        # Log the error using Allure
        allure.attach(f"Error while finding source ID: {str(e)}", name="Error", attachment_type=allure.attachment_type.TEXT)
        logging.error(f"Error while finding source ID: {str(e)}")
    return None

def find_properties(data, source_id_to_find):
    try:
        for item in data.get('data', []):
            source_id = item.get('Properties', {}).get('p14')
            if source_id == source_id_to_find:
                return source_id
    except (KeyError, AttributeError) as e:
        # Log the error using Allure
        allure.attach(f"Error while finding properties: {str(e)}", name="Error", attachment_type=allure.attachment_type.TEXT)
        logging.error(f"Error while finding properties: {str(e)}")
    return None

def verify_sourceID(data, source_id_to_find):
    if data is not None:
        try:
            source_id = find_source_id(data, source_id_to_find)
            if source_id is not None:
                assert source_id == source_id_to_find
            else:
                # Log the error using Allure
                allure.attach(f"SourceID '{source_id_to_find}' not found in the response.", name="Error", attachment_type=allure.attachment_type.TEXT)
                logging.error(f"SourceID '{source_id_to_find}' not found in the response.")
        except AssertionError as e:
            # Log the error using Allure
            allure.attach(f"Assertion error: {str(e)}", name="Error", attachment_type=allure.attachment_type.TEXT)
            logging.error(f"Assertion error: {str(e)}")
    else:
        # Log the error using Allure
        allure.attach("Failed to retrieve data from the URL.", name="Error", attachment_type=allure.attachment_type.TEXT)
        logging.error("Failed to retrieve data from the URL.")
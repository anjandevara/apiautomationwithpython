import allure
from modules.sourcelatestdata import get_data_from_url, verify_sourceID
from utils.confest import *

methodname = 'GET'

# ------------------------------------------TC-001----------------------------------------------------------
# Use Allure to create a test case with a name
@allure.feature("Data Retrieval")
@allure.story("Retrieve Data from URL")
@allure.title("Retrieve data using GET method")
@allure.epic("Retrieval")
@allure.id("TC-001")
@allure.description("This test case retrieves data from a URL using the GET method.")
@allure.description_html("<b>Description:</b> This test case retrieves data from a URL using the GET method.")
@allure.issue("LINK-123", name="Related Issue")
@allure.label("Test Type", "Functional")
@allure.link("https://example.com", name="Related Link")
@allure.manual("Step 1: Perform data retrieval")
@allure.parent_suite("Parent Suite")
@allure.severity(allure.severity_level.NORMAL)
@allure.sub_suite("Sub Suite")
@allure.suite("Test Suite")
@allure.tag("Regression")
@allure.testcase("Test Case Title")
def test_01_data_retrieval():
    # Use Allure steps to mark individual actions
    with allure.step("Performing data retrieval using GET method"):
        result = get_data_from_url(methodname, url, headers, credentials)
        if result is not None:
            print(result)

# ------------------------------------------TC-002----------------------------------------------------------
@allure.feature("Data Searching")
@allure.story("Searching SOURCE ID")
@allure.title("Data Searching using GET method")
@allure.epic("Searching")
@allure.id("TC-002")
@allure.description("This test case searches for a SOURCE ID using the GET method.")
@allure.issue("LINK-456", name="Related Issue")
@allure.label("Test Type", "Functional")
@allure.link("https://example.com", name="Related Link")
@allure.manual("Step 1: Perform data retrieval for searching\nStep 2: Verify SOURCE ID")
@allure.parent_suite("Parent Suite")
@allure.severity(allure.severity_level.CRITICAL)
@allure.sub_suite("Sub Suite")
@allure.suite("Test Suite")
@allure.tag("Regression")
@allure.testcase("Test Case Title")
def test_02_sample_without_payload():
    # Use Allure steps to mark individual actions
    with allure.step("Performing data retrieval using GET method for searching"):
        data = get_data_from_url(methodname, url, headers, credentials)

    # Use Allure steps to mark the verification step
    with allure.step("Verifying SOURCE ID"):
        verify_sourceID(data, "CARU0000039")

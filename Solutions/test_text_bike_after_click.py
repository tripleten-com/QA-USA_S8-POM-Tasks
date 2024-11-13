import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


def test_custom_bike_option():
    driver = webdriver.Chrome()
    # Step 1: Open the app - update the URL after starting the server
    driver.get('https://cnt-fd677479-89ab-4ea3-ad09-0999796f6ec8.containerhub.tripleten-services.com')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 3: Use POM methods to perform actions on the page
    # Enter "From" and "To" locations.
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Select the "Custom" option.
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the "Bike" icon.
    urban_routes_page.click_bike_icon()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 4: Verify the Bike text is displayed correctly
    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bike"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    driver.quit()


def test_duration_custom_bike_option():
    driver = webdriver.Chrome()
    # Step 1: Open the app - update the URL after starting the server
    driver.get('https://cnt-fd677479-89ab-4ea3-ad09-0999796f6ec8.containerhub.tripleten-services.com')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 3: Use POM methods to perform actions on the page
    # Enter "From" and "To" locations.
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Select the "Custom" option.
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the "Bike" icon.
    urban_routes_page.click_bike_icon()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 4: Verify the Duration text is displayed correctly
    actual_value = urban_routes_page.get_duration_text()
    expected_value = "Duration"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    driver.quit()
import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


def test_custom_bike_option():
    driver = webdriver.Chrome()
    # Update server URL
    driver.get('https://cnt-dd3ea7cf-991c-4e39-8316-2f92a9b80a12.containerhub.tripleten-services.com')
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_bike_icon()
    time.sleep(2)
    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bike"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    actual_value = urban_routes_page.get_duration_text()
    expected_value = "Duration"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    driver.quit()
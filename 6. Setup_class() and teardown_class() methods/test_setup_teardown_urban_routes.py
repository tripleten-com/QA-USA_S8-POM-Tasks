from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage


# Create a class for both tests
class TestUrbanRoutes:

    # Initialize the Chrome driver once for the class
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()


    def test_custom_bike_option(self):
        self.driver.get('https://cnt-8f25f166-edc1-4f8d-b177-7e4079036890.containerhub.tripleten-services.com')

        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_locations(
            'East 2nd Street, 601',
            '1300 1st St'
        )

        urban_routes_page.click_custom_option()

        time.sleep(2)

        urban_routes_page.click_bike_icon()

        time.sleep(2)

        actual_value = urban_routes_page.get_bike_text()
        expected_value = "Bike"

        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"


    def test_duration_custom_bike_option(self):
        self.driver.get('https://cnt-8f25f166-edc1-4f8d-b177-7e4079036890.containerhub.tripleten-services.com')

        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_locations(
            'East 2nd Street, 601',
            '1300 1st St'
        )

        urban_routes_page.click_custom_option()

        time.sleep(2)

        urban_routes_page.click_bike_icon()

        time.sleep(2)

        actual_value = urban_routes_page.get_duration_text()
        expected_value = "Duration"

        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"


    # Close the browser after all tests are done
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

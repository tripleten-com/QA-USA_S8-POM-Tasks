import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


def test_drive_custom_camping_option():
    driver = webdriver.Chrome()
    # Open the app - update the URL after starting the server
    driver.get('https://cnt-41064ba9-4507-4af6-8029-636eaab78c0d.containerhub.tripleten-services.com')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 1: Enter the "From" address
    urban_routes_page.enter_from_location('East 2nd Street, 601')

    # Step 2: Enter the "To" address
    urban_routes_page.enter_to_location('1300 1st St')

    # Step 3: Choose "Custom"
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 4: Click "Drive"
    urban_routes_page.click_drive_icon()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 5: Click "Book"
    urban_routes_page.click_book_button()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 6: Choose "Camping"
    urban_routes_page.click_camping()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 7: Check if the text displays "Audi A3 Sedan"
    actual_value =  urban_routes_page.get_audi_text()
    expected_value = "Audi A3 Sedan"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got {actual_value}'"
    driver.quit()

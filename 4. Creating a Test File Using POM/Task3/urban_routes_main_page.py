from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = ...
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = ...
    CAMPING_LOCATOR = ...
    ADD_DRIVER_LICENSE_LOCATOR = ...
    FIRST_NAME_LOCATOR = ...
    LAST_NAME_LOCATOR = ...
    DATE_OF_BIRTH_LOCATOR = ...
    NUMBER_LOCATOR = ...
    ADD_BUTTON_LOCATOR = ...
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    VERIFICATION_TEXT_LOCATOR = ...

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        ...

    def enter_to_location(self, to_text):
        # Enter To
        ...

    def click_custom_option(self):
        # Click Custom
        ...

    def click_drive_icon(self):
        # Click Drive Icon
        ...

    def click_book_button(self):
        # Click Book Button
        ...

    def click_camping(self):
        # Click Camping
        ...

    def click_add_driver_license(self):
        # Click Add Driver's Licence
        ...

    def enter_first_name(self, first_name):
        # Enter First Name
        ...

    def enter_last_name(self, last_name):
        # Enter Last Name
        ...

    def enter_date_of_birth(self, date_of_birth):
        # Enter Date of Birth
        ...

    def enter_number(self, number):
        # Enter Number
        ...

    def click_title(self):
        # Click Add a Driver's License Title
        ...

    def click_add_button(self):
        # Click Add Button
        ...

    def get_verification_text(self):
        # Return the verification text
        ...
from selenium.webdriver.common.by import By

# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_LOCATOR = (By.XPATH, '//div[contains(text(),"Camping")]')
    AUDI_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Audi A3 Sedan")]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '(//div[contains(text(),"Add a driver")])[2]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Add"]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@style="margin-bottom: 30px;"]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_custom_option(self):
        # Click Custom
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_drive_icon(self):
        # Click Drive Icon
        self.driver.find_element(*self.DRIVE_ICON_LOCATOR).click()

    def click_book_button(self):
        # Click Book Button
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def click_camping(self):
        # Click Camping
        self.driver.find_element(*self.CAMPING_LOCATOR).click()

    def get_audi_text(self):
        # Return the "Audi" text
        return self.driver.find_element(*self.AUDI_TEXT_LOCATOR).text

    def click_add_driver_license(self):
        # Click Add Driver's Licence
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_LOCATOR).click()

    def enter_first_name(self, first_name):
        # Enter First Name
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Enter Last Name
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        # Enter Date of Birth
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).send_keys(date_of_birth)

    def enter_number(self, number):
        # Enter Number
        self.driver.find_element(*self.NUMBER_LOCATOR).send_keys(number)

    def click_title(self):
        # Click Add a Driver's License Title
        self.driver.find_element(*self.ADD_A_DRIVER_LICENCE_TITLE_LOCATOR).click()

    def click_add_button(self):
        # Click Add Button
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    def get_verification_text(self):
        # Return the verification text
        return self.driver.find_element(*self.VERIFICATION_TEXT_LOCATOR).text

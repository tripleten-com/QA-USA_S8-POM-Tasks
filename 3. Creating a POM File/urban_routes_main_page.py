from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributesfrom selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from') .send_keys('East 2nd Street, 601')
    TO_LOCATOR = (By.ID, 'to') .send_keys('1300 1st St')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike-active.b0d16d8b.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[@class="text">Bike ~ $1</div]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys('East 2nd Street, 601')

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys('1300 1st St')

    def click_custom_option(self):
        # Click the "Custom" option
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_bike_icon(self):
        # Click the "Bike" icon
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def get_bike_text(self):
        # Return the "Bike" text
        return self.driver.find_element(*self.BIKE_TEXT_LOCATOR).text
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    BIKE_ICON_LOCATOR = ...
    BIKE_TEXT_LOCATOR = ...

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_custom_option(self):
        # Click the "Custom" option
        ...

    def click_bike_icon(self):
        # Click the "Bike" icon
        ...

    def get_bike_text(self):
        # Return the "Bike" text
        ...

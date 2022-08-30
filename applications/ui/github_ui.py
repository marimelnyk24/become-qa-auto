from providers.data.users_provider import UsersProvider
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GitHubUI:

    def __init__(self, base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

    def login(self, username, userpassword):
        self.driver.get(f"{self.base_url}/login")
        elem = self.driver.find_element(By.ID, "login_field")
        elem.send_keys(username)

        elem = self.driver.find_element(By.ID, "password")
        elem.send_keys(userpassword)

        elem.send_keys(Keys.RETURN)

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

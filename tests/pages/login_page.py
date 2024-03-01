from seleniumpagefactory import PageFactory


class By:
    ID = 'ID'
    XPATH = 'XPATH'
    TAG_NAME = 'TAG'


class LoginPage(PageFactory):
    locators = {
        'username': (By.ID, 'username'),
        'password': (By.ID, 'password'),
        'button': (By.TAG_NAME, 'button'),
        'flash': (By.ID, 'flash'),
    }

    def __init__(self, driver):
        self.driver = driver

    def login(self, username='', password=''):
        self.username.set_text(username)
        self.password.set_text(password)
        self.button.click()

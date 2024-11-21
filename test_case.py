import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PythonSeleniumDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'path_to_chromedriver')

    def test_first_example(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")
        title = driver.title
        self.assertEqual(title, "Wikipedia")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

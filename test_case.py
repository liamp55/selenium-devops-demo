import unittest
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://wikipedia.com")

    def test_title(self):
        self.assertEqual(self.driver.title, "Wikipedia", "Inequal title")
        

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    
if __name__ == "__main__":

    unittest.main()

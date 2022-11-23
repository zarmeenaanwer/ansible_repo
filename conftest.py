import pytest
from selenium import webdriver
#from webdriver_manager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
 ser_obj = Service("C://Program Files//chromedriver2.exe")
 driver = webdriver.Chrome(service=ser_obj)
     #executable_path=ChromeDriverManger().install())
 driver.maximize_window()
 driver.get("https://demo.nopcommerce.com/")
 request.cls.driver = driver



 yield
 driver.close()
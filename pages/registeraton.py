import self
from selenium.webdriver.common.by import By

class registration():
    def     __int__(self,driver):
        self.driver = driver
    currency=self.driver.find_element(By.XPATH, "//*[@id='customerCurrency']").click()
    self.find_element(By.XPATH, "//*[@id='customerCurrency']/option[2]").click()
    self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    gender=self.find_element(By.XPATH, "//span[@class='female']").click()
    ID =self.find_element(By.ID, "FirstName").send_keys("Zarmeena")
    self.find_element(By.NAME, "LastName").send_keys("Anwer")
    self.find_element(By.XPATH, "//select[@name='DateOfBirthDay']").send_keys("12")
    self.find_element(By.XPATH, "//select[@name='DateOfBirthDay']").send_keys("June")
    self.find_element(By.NAME, "DateOfBirthYear").send_keys("1993")
    self.find_element(By.ID, "Email").send_keys("dewewpiiuIiaPIiOi@gmail.com")
    self.find_element(By.ID, "Company").send_keys("alnafi.co")
    self.find_element(By.ID, "Password").send_keys("1234567")
    self.find_element(By.ID, "ConfirmPassword").send_keys("1234567")
    self.find_element(By.XPATH, "//button[@id='register-button']").click()

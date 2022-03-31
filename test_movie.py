from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setup():
    global Mname,year,Director,Distributor,Producer,driver
    Mname = input("enter the movie name")
    year=input("enter year")
    Director=input("enter director name")
    Distributor=input("enter distributor")
    Producer=input("enter producer name")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time .sleep(10)
    driver.close()


def test_movie(setup):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(Mname)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(Director)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(Distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(Producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[5]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(5)
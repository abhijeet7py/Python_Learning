import pytest
import allure
import requests

@allure.title("Test Get Request - Restful Booker")
@allure.description("TC#1- Verify that GET Request with ID works")
@allure.tag("regression","P0","Smoke")
@allure.label("owner","Abhijeet")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 200
    print(response_data.url)
    print(response_data.json())

@allure.title("Test Get Request - Restful Booker")
@allure.description("TC#2- Verify that GET Request with ID works")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404

@allure.title("Test Get Request - Restful Booker")
@allure.description("TC#3- Verify that GET Request with ID works")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id_negative_2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404

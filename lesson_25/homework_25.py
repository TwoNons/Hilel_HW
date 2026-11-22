import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

XPATH = [
    "//a[contains(@class, 'header_logo')]",  # 1. Логотип
    "//button[normalize-space()='Sign In']",  # 2. Кнопка Sign In
    "//button[normalize-space()='Sign up']",  # 3. Кнопка Sign Up
    "//button[contains(normalize-space(), 'Guest log in')]",  # 4. Guest log in
    "//div[contains(@class, 'modal')]//input[@id='signinEmail']",  # 5. Email
    "//div[contains(@class, 'modal')]//input[@id='signinPassword']",  # 6. Password
    "//div[contains(@class, 'modal')]//button[normalize-space()='Login']",  # 7. Login
    "//div[contains(@class, 'modal')]//a[contains(text(), 'Forgot password')]",  # 8. Forgot password
    "//div[contains(@class, 'modal')]//input[@id='signupName']",  # 9. Имя
    "//div[contains(@class, 'modal')]//input[@id='signupLastName']",  # 10. Фамилия
    "//div[contains(@class, 'modal')]//input[@id='signupEmail']",  # 11. Email регистрации
    "//div[contains(@class, 'modal')]//input[@id='signupPassword']",  # 12. Пароль регистрации
    "//div[contains(@class, 'modal')]//input[@id='signupRepeatPassword']",  # 13. Повтор пароля
    "//div[contains(@class, 'modal')]//button[normalize-space()='Register']",  # 14. Register
    "//nav//a[normalize-space()='Garage']",  # 15. Garage
    "//app-garage//button[contains(., 'Add car')]",  # 16. Add car
    "//app-add-car-modal//select[@id='addCarBrand']",  # 17. Brand
    "//app-add-car-modal//select[@id='addCarModel']",  # 18. Model
    "//app-add-car-modal//input[@id='addCarMileage']",  # 19. Mileage
    "//app-add-car-modal//button[normalize-space()='Add']",  # 20. Add
    "//nav//a[contains(@routerlink, 'expenses')]",  # 21. Fuel expenses
    "//nav//a[contains(@routerlink, 'instructions')]",  # 22. Instructions
    "//button[@id='userNavDropdown']",  # 23. Profile
    "//nav[contains(@class, 'dropdown-menu')]//button[contains(., 'Logout')]",  # 24. Logout
    "//div[contains(@class, 'modal-dialog')]//button[@type='button']",  # 25. Кнопки модального окна
]

CSS = [
    "a.header_logo",  # 1. Логотип
    "button.header_signin",  # 2. Кнопка Sign In
    "button.header_signup",  # 3. Кнопка Sign Up
    "button.header-link",  # 4. Guest log in
    "div.modal input#signinEmail",  # 5. Email
    "div.modal input#signinPassword",  # 6. Password
    "div.modal button.btn-primary",  # 7. Login
    "div.modal a.btn-link",  # 8. Forgot password
    "div.modal input#signupName",  # 9. Имя
    "div.modal input#signupLastName",  # 10. Фамилия
    "div.modal input#signupEmail",  # 11. Email регистрации
    "div.modal input#signupPassword",  # 12. Пароль регистрации
    "div.modal input#signupRepeatPassword",  # 13. Повтор пароля
    "app-signup-modal div.modal-footer button.btn-primary",  # 14. Register
    "nav a[routerlink='/panel/garage']",  # 15. Garage
    "app-garage button.btn-primary",  # 16. Add car
    "app-add-car-modal select#addCarBrand",  # 17. Brand
    "app-add-car-modal select#addCarModel",  # 18. Model
    "app-add-car-modal input#addCarMileage",  # 19. Mileage
    "app-add-car-modal button.btn-primary",  # 20. Add
    "nav a[routerlink='/panel/expenses']",  # 21. Fuel expenses
    "nav a[routerlink='/panel/instructions']",  # 22. Instructions
    "button#userNavDropdown",  # 23. Profile
    "nav.dropdown-menu button.btn-logout",  # 24. Logout
    "div.modal-dialog button[type='button']",  # 25. Кнопки модального окна
]
browser = WebDriver()
browser.maximize_window()
browser.get("<https://UserName:Password@qauto2.forstudy.space>;")
time.sleep(5)

for i in XPATH:
	browser.find_element(By.XPATH, i)
for j in CSS:
	browser.find_element(By.CSS_SELECTOR, j)

browser.quit()
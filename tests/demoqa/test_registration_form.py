import allure
from qa_guru_9_13.pages.registration_page import RegistrationPage


@allure.title('Seccessful fill form')
def test_student_registration_form():
    registration_page = RegistrationPage()

    with allure.step('Open registration page'):
        registration_page.open()
    with allure.step('Fill registration form'):
        registration_page.fill_first_name('Alex')
        registration_page.fill_last_name('Davydov')
        registration_page.fill_email('AlexDavydov92@gmail.com')
        registration_page.fill_gender()
        registration_page.fill_user_number('8005553535')
        registration_page.fill_birthday("1992", "June", "20")
        registration_page.fill_subjects('English')
        registration_page.fill_hobbies()
        registration_page.fill_picture('selfies.jpeg')
        registration_page.fill_address('South Street')
        registration_page.fill_state('Haryana')
        registration_page.fill_city('Karnal')
        registration_page.fill_submit()
    with allure.step('Check if registration was successful'):
        registration_page.should_registered_user_with(
            'Alex Davydov',
            'AlexDavydov92@gmail.com',
            'Male',
            '8005553535',
            '20 June,1992',
            'English',
            'Reading',
            'selfies.jpeg',
            'South Street',
            'Haryana Karnal',
        )

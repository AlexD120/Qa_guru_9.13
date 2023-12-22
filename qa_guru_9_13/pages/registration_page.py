from selene import browser, have, be, by
from selene.support.shared.jquery_style import s
from qa_guru_9_13 import resource


class RegistrationPage:
    def __init__(self):
        self.first_name = s('#firstName')
        self.last_name = s('#lastName')
        self.state = s('#react-select-3-input')
        self.email = s('#userEmail')
        self.gender = s('#gender-radio-1')
        self.user_number = s('#userNumber')
        self.subjects = s('#subjectsInput')
        self.hobbies = s("[for='hobbies-checkbox-2']")
        self.picture = s('#uploadPicture')
        self.address = s('#currentAddress')
        self.city = s('#react-select-4-input')
        self.submit = s('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        s('.pattern-backgound').should(have.exact_text('Practice Form'))
        return self

    def fill_first_name(self, value):
        self.first_name.should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.should(be.blank).type(value)
        return self

    def fill_email(self, value):
        self.email.should(be.blank).type(value)
        return self

    def fill_gender(self):
        self.gender.double_click()
        return self

    def fill_user_number(self, number):
        self.user_number.type(number)
        return self

    def fill_birthday(self, year, month, day):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click().element(by.text(month)).click()
        s('.react-datepicker__year-select').click().element(by.text(year)).click()
        s(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, subjects_name):
        self.subjects.should(be.blank).type(subjects_name).press_enter()
        return self

    def fill_hobbies(self):
        self.hobbies.click()
        return self

    def fill_picture(self, value):
        self.picture.send_keys(resource.path(value))
        return self

    def fill_address(self, adress):
        self.address.should(be.blank).type(adress)
        return self

    def fill_state(self, state_name):
        self.state.type(state_name).press_enter()
        return self

    def fill_city(self, city_name):
        self.city.type(city_name).press_enter()
        return self

    def fill_submit(self):
        self.submit.press_enter()
        return self

    def should_registered_user_with(
        self,
        full_name,
        email,
        gender,
        number,
        date_of_birth,
        subjects,
        hobbies,
        file,
        current_address,
        state_and_city,
    ):
        s('.table-responsive').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                file,
                current_address,
                state_and_city,
            )
        )
        return self

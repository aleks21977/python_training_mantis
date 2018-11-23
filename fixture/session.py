

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        #        wd.find_element_by_name("username").click() # это не обязательно делать но в уроке оно есть
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        #        wd.find_element_by_name("password").click() # это не обязательно делать но в уроке оно есть
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0 # если на странице есть хотя бы один елемент с именем Logout

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text # поиск имени вошедшего пользоватлея

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in(): # если пользователь не залогинин
            if self.is_logged_in_as(username): # если вошли в систему как пользователь например admin
                return # то возврат и делать ничего не нужно
            else: # если пользователь не тот
                self.logout() # то logout
        self.login(username, password) # войти под нужным пользователем



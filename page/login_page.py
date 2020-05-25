from selenium.webdriver.common.by import By

from base.base_action import Base_action
from base.driver import init_dirver


class Login_page(Base_action):
    def __init__(self,driver):
        Base_action.__init__(self,driver)
    # 打开浏览器
    def open(self):
        self.open_app('com.achievo.vipshop','.homepage.activity.MainActivity')
    # 点击消息按钮
    def message_click(self):
        self.click_element(By.ID,'com.achievo.vipshop:id/tips_icon')
    # 清空用户名
    def clear_text(self):
        self.clear_element(By.ID, 'com.achievo.vipshop:id/username')

    # 清空并输入输入用户名
    def send_name(self,name):
        self.send_keys(By.ID,'com.achievo.vipshop:id/username',name)
    # 输入密码    
    def send_password(self,value):
        self.send_keys(By.ID,'com.achievo.vipshop:id/password',value)
    # 点击登录按钮
    def login_click(self):
        self.click_element(By.ID,'com.achievo.vipshop:id/login')
    # 抓取toast
    def toast(self,message):
        ele=self.find_element(By.XPATH,'//*[contains(@text,"'+ message +'")]')
        return ele.text
    # 判断
    def panduan(self):
        if self.toast('成功'):
            assert 1
        else:
            assert 0
    # 按键返回
    def press_back(self):
        self.back_keyevent()
    # 点击右下角图标
    def click_location_login(self):
        self.click_location(50,1210)
        # 点击设置按钮
    def click_setting_button(self):
        self.click_element(By.ID,'com.achievo.vipshop:id/btn_setting')
    # 点击退出按钮
    def click_exit_button(self):
        self.click_element(By.ID,'com.achievo.vipshop:id/bt_logout')
    # 确认退出
    def click_enter(self):
        self.click_element(By.ID,'com.achievo.vipshop:id/vip_dialog_normal_right_button')


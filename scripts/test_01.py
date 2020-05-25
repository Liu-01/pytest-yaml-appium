import pytest
import yaml
import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By

from base.driver import init_dirver
from page.login_page import Login_page
import os,sys
sys.path.append(os.getcwd())
import time

# 读取yml的数据
def read_data(filename):
    with open('./data/' + filename + '.yml', 'r') as f:
        data = yaml.safe_load(f)
        return data

# 获取以字典嵌套的数据的字典的值
def read_data_with_key(key):
    data = read_data('data')[key]
    data_list = list()
    for case_data in data.values():
        data_list.append(case_data)
    return data_list




class Test_01():

    def setup(self):
        self.driver=init_dirver()
        self.newdriver=Login_page(self.driver)
        print('start')
    # 数据参数化
    @pytest.mark.parametrize('value',read_data_with_key('test_01'))
    def test_001(self,value):
        # 打开app
        self.newdriver.open()
        # 点击消息按钮
        self.newdriver.message_click()
        # 清空文本框
        self.newdriver.clear_text()
        # 输入用户名
        self.newdriver.send_name(value['name'])
        # 输入密码
        self.newdriver.send_password(value['password'])
        # 点击登录
        self.newdriver.login_click()
        # 如果可以抓到toast包含成功那么认为测试成功
        try:
            if '成功'in self.newdriver.toast('成功'):
                assert 1
            # 点击返回键
            self.newdriver.back_keyevent()
            # 等待抓取返回页面
            time.sleep(5)
            # 点击左下角按钮
            self.newdriver.click_location_login()
            # 点击设置
            self.newdriver.click_setting_button()
            # 点击退出
            self.newdriver.click_exit_button()
            # 确认退出
            self.newdriver.click_enter()
            # 关闭
            self.driver.quit()

        except:
            assert 0
            self.driver.quit


        # self.newdriver.toast('成功')
        # self.newdriver.panduan()
        # self.newdriver.back_keyevent()
        # time.sleep(5)
        # self.newdriver.click_location_login()
        # self.newdriver.click_setting_button()
        # self.newdriver.click_exit_button()
        # self.newdriver.click_enter()
        # self.driver.quit()


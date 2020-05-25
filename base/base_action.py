from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.driver import init_dirver



class Base_action():
    def __init__(self,driver):
        self.driver=driver
    # 打开APP
    def open_app(self,app_package,app_activity):
        self.driver.start_activity(app_package=app_package,app_activity=app_activity)
    def find_element(self,by,value):
        return WebDriverWait(self.driver,20,0.5).until(lambda x:x.find_element(by,value))
    # 点击元素
    def click_element(self,by,value):
        self.find_element(by,value).click()
    # 通过坐标点击
    def click_location(self,x,y):
        TouchAction(self.driver).tap(x=x,y=y).perform()
    def click_location2(self,x,y):
        TouchAction(self.driver).press(x=x,y=y).release().perform()
    def clear_element(self,by,value):
        self.find_element(by,value).clear()
    # 输入文字
    def send_keys(self,by,value1,value2):
        self.find_element(by,value1).send_keys(value2)
    # 坐标滑动屏幕
    def swip_sceen__by_location(self,start_x,start_y,end_x,end_y):
        self.driver.swipe(start_x=start_x,start_y=start_y,end_x=end_x,end_y=end_y)
    # 获取屏幕分辨率
    def get_window_size(self):
        return self.driver.get_window_size()
    # 滑动屏幕
    def swip_half_screen(self):
        width=self.get_window_size().get('width')
        height=self.get_window_size()['height']
        self.driver.swipe(width*0.5,height*0.9,width*0.5,height*0.1)
    # 滑动屏幕通过元素
    def scroll_screen(self,by,value,by1,value1):
        self.driver.scroll(origin_el=self.find_element(by,value),destination_el=self.find_element(by1,value1),duration=1000)
    # 滑动方法二
    def drag_and_drop(self,by,value,by1,value1):
        self.driver.drag_and_drop(origin_el=self.find_element(by,value),destination_el=self.find_element(by1,value1),duration=1000)
    # 通过元素长按
    def long_press_screen_element(self,by,value):
        TouchAction(self.driver).long_press(self.find_element(by,value),duration=3000).perform()
    # 通过坐标长按
    def long_press_screen_location(self,x,y):
        TouchAction(self.driver).long_press(x=x,y=y).perform()
    # 返回键
    def back_keyevent(self):
        self.driver.press_keycode(4)
    # 菜单键
    def menu_keyevent(self):
        self.driver.press_keycode(82)
    # 获取页面属性
    def get_window_page_souce(self):
        return self.driver.page_source
    # 获取元素坐标
    def get_element_location(self,by,value):
        return self.find_element(by,value).location
    # 打开通知栏
    def open_notifications(self):
        self.driver.open_notifications()
    # 查看网络连接
    def get_network_connection(self):
        return self.driver.network_connection
    # 设置网络连接
    def set_network_connection(self,value):
        self.driver.set_network_connection(value)
        # 0(None) 1 (Airplane Mode) 2 (Wifi only)
        # 4(Data only) 6 (All network on)
    # 截图存到screen目录下
    def get_screenshot_as_file(self,filename):
        self.driver.get_screenshot_as_file('./screen'+ filename +'.png')
    # 通过坐标滑动方法
    def move_to_location(self,x1,y1,x2,y2):
        TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).perform()
    # toast
    def toast(self,message):
        return self.find_element(By.XPATH,'//*[contains(@text,"'+ message +'")]').text
    # 关闭
    def quit(self):
        self.driver.quit()

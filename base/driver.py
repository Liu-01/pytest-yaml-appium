'''
这里构建一个安卓驱动
'''
from appium import webdriver


def init_dirver():
    desired_caps=dict()
    # 系统名
    desired_caps['platformName']='Android'
    # 设备版本
    desired_caps['platformVersion']='5.1.1'
    # 设备名
    desired_caps['deviceName']='116cfa91'
    # 包名
    desired_caps['appPackage']='com.android.settings'
    # 启动名
    desired_caps['appActivity']='.Settings'
    # 允许中文输入
    desired_caps['unicodeKeyboard']='True'
    # 收起键盘
    desired_caps['resetKeyboard']='True'
    # 自动打开程序
    desired_caps['autoLaunch']='False'
    # 重置应用
    desired_caps['noReset']='True'
    # toast
    desired_caps['automationName']='uiautomator2'
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return driver
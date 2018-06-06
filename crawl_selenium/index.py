from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()



chrome_options = Options()
chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
driver = webdriver.Chrome(chrome_options=chrome_options)

# ========================================================================
# print('======打开浏览器====之药监局=====')
# driver.get("http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=19&tableName=TABLE19&title=%E8%8D%AF%E7%89%A9%E4%B8%B4%E5%BA%8A%E8%AF%95%E9%AA%8C%E6%9C%BA%E6%9E%84%E5%90%8D%E5%8D%95&bcId=118714941832181502104731901420")

# method 1
# centerData = driver.find_elements_by_xpath("//*[@id='content']/div/table/tbody")
# print(centerData[1].text)

# method 2
# centerData = driver.find_elements(By.XPATH,"//*[@id='content']/div/table/tbody")
# print(centerData[1].text)

# method 3
# javaScript="return document.getElementById('content').children[0].children;"
# centerData = driver.execute_script(javaScript)
# print(centerData[1].text)

# listData = centerData[1]
# print(listData.text)
# driver.quit()
# quit()


# ========================================================================
print('======打开浏览器====之淘宝————关联推荐=====')

def getFinalElement(url) :
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "J_TabBarBox"))
        )
    except TimeoutException:
        return False

    if is_recommends_appear(driver):
        print(u'已经成功加载出下方橱窗推荐宝贝信息')
        return driver.page_source


def is_recommends_appear(driver, max_time=10):
    count = 1
    result = scroll_bottom_recommends(driver, count)
    while not result:
        count = count + 1
        result = scroll_bottom_recommends(driver, count)
        if count == max_time:
            return False
    return True


def scroll_bottom_recommends(driver, count):
    print(u'正在尝试第', count, u'次下拉')
    try:
        js = "window.scrollTo(0,document.body.scrollHeight-" + str(count * count* 100) + ")"
        driver.execute_script(js)
    except WebDriverException:
        print(u'下拉寻找橱窗宝贝时出现问题')
    time.sleep(2)

    try:
        driver.find_element_by_css_selector('#J_TjWaterfall li')
    except NoSuchElementException:
        return False

    return True


url = "https://world.tmall.com/item/45262540681.htm?spm=a220m.1000858.1000725.110.r7oyq2&id=45262540681&areaId=320700&cat_id=50025145&rn=6f644caecfa85abefea71e2dc48ac6ae&user_id=2148264599&is_b=1"
getFinalElement(url)

DD = driver.find_elements_by_xpath("//*[@id='J_Detail']/div[@id='J_TabRecommends']/*/ul[@id='J_TjWaterfall']/li")

print(DD[0].text)
print(DD[0].find_element('tag name','a').get_attribute('href'))
print(DD[0].find_element('tag name','img').get_attribute('src'))
print(DD[1].text)

print(DD[1].find_element('tag name','a').get_attribute('href'))
print(DD[1].find_element('tag name','img').get_attribute('src'))



driver.quit()
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
driver = webdriver.Chrome('/Users/admin/Downloads/chromedriver')

class Nike:

    def __init__(self):
        self.login()
        self.findSizeInput()
        self.order()
        # self.payment()

    def login(self):

        # 쿠키 담기
        cookies = "자신의 쿠키를 넣어주세요"

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(
            'https://www.nike.com/kr/ko_kr/t/adult-unisex/fw/football-soccer/AQ4174-001/fiuv99/superfly-7-elite-fg')

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get(
            'https://www.nike.com/kr/ko_kr/t/adult-unisex/fw/football-soccer/AQ4174-001/fiuv99/superfly-7-elite-fg')


    def findSizeInput(self):

        time.sleep(0.5)
        # 사이즈 찾기
        driver.find_element_by_xpath('/html/body/section/section/section/article/article[2]/div/div[4]/div/div[2]/form/div[1]/div[2]/div[1]/div/span[8]').click()

        time.sleep(0.5)
        # 바로 구매 버튼 클릭
        driver.find_element_by_xpath('//*[@id="btn-buy"]').click()

    def order(self):
        time.sleep(0.5)
        driver.find_element_by_xpath('// *[ @ id = "btn-next"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('// *[ @ id = "payment-review"] / div[1] / ul / li[1] / div / div[1] / h6').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span/label/span').click()
        time.sleep(3)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="complete_checkout"]').click()

        # 결제
        iframe = driver.find_element_by_xpath("/html/body/div[13]/iframe[2]")
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[2]/a').click()
        driver.find_element_by_id('userPhone').send_keys('01056741111')


if __name__ == "__main__":
    nike = Nike()
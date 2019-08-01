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
        cookies = [
{
    "domain": ".nike.com",
    "expirationDate": 1596212544.049667,
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "_abck",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "true",
    "session": "false",
    "storeId": "0",
    "value": "A7F1A30D5F748467ABA42976556EA95F~-1~YAAQL0vIF2/XSeJrAQAAVlr9TQLZL/sOMIOaYBlZcGvCJ/OJK9XVzomh6Z3pctRa9ArwvqDz9s7TJx7pTieAbAaHA9nhIwtcRORVBdmjC5IIp0RJ0bLrJhFSeb0Pos2fs0egkFcQmjYjLpyR4TgOH40r1WiGQNqPQjhHb0sMokWIT5l4ZDzqmgIlmiV/hBiV5YiA5WnPB+Zmbwe4nvWOHbx2x/DZvEpwoCsgT6NvPwSVMMTcyzigNeUi+wRHpLsJecqc/GOyVMQiqBq0vw1WtbEwul3wdBw4oYGTOtg9kVra7MQLn9DX1w2kouluETFDVIg9Qt/pFtMAnu9IMbZqOeV8uYDTresbPA==~-1~-1~-1",
    "id": 1
},
{
    "domain": ".nike.com",
    "expirationDate": 1564683736.450106,
    "hostOnly": "false",
    "httpOnly": "true",
    "name": "ak_bmsc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "72F9BF8B8AB899DB0DBC95C1E7E9759B17C84B2F81780000B911435DE525E410~plieMyM/6c+BlIbNe5DPQE6berNUcLk/IT6iabVLyWJ6tCgr+czcq8I1NKEDm76xhyrQbWIF25fthUAL0MItpAhpkUzLkDNMQMCYv6RL3P3ICT46TdDOVXVmHs930wqwJEfRPUp6HK8z1xgMraqtFjJi4zicPvcbQKdVvu63JKQPoMSXevcG2a7s3yHgvcFb5NJMCpMLXNmOr0Ck/OmBdrVHbMvL9PhxowXVXQWmWkjnLtkvDgYo224NH4FGrfW6lPabjb9aPcCASkQ1IDnRdb2sStmN+NhVYVSg3UqSo2Q9Q5ImpU4lODOhI3QtFMUWAwgZyqQhquQ3G7MtxIIZPI+A==",
    "id": 2
},
{
    "domain": ".nike.com",
    "expirationDate": 1564680136.421811,
    "hostOnly": "false",
    "httpOnly": "true",
    "name": "AKA_A2",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "true",
    "session": "false",
    "storeId": "0",
    "value": "A",
    "id": 3
},
{
    "domain": ".nike.com",
    "expirationDate": 1627834943,
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "AMCV_F0935E09512D2C270A490D4D%40AdobeOrg",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "-715282455%7CMCIDTS%7C18109%7CMCMID%7C10223119284961012873355719364343489608%7CMCAID%7CNONE%7CMCOPTOUT-1564683743s%7CNONE%7CvVersion%7C4.2.0",
    "id": 4
},
{
    "domain": ".nike.com",
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "true",
    "storeId": "0",
    "value": "1",
    "id": 5
},
{
    "domain": ".nike.com",
    "expirationDate": 1564683736.100095,
    "hostOnly": "false",
    "httpOnly": "true",
    "name": "bm_sv",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "EF9E6C2BE16A546211729F3C271809FE~7R45Tv13sfxknmXGd6yvQNSwKGmAoCfNSnRqRpVXtOhzI8qFR1BrZG1tsM5/0AXnqv+IzmTMPop3CFJ/5eONXWF3Gb2MsBrqBuAIWhQUAG/Bu+iHB0nsSJflDQgT15vDqX70PkU2ZisuFBzpARwKJA==",
    "id": 6
},
{
    "domain": ".nike.com",
    "expirationDate": 1564690936.421886,
    "hostOnly": "false",
    "httpOnly": "true",
    "name": "bm_sz",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "498CDAB73D5A4B290B98B30672C303BD~YAAQL0vIFy3XSeJrAQAAijz9TQQUo3WlMMr+uE4TOm+19Dfw9cLUAOqpdCLM5A2/zMRMnyg8olZrA8E2+TjMyXiq+/ws1F3uFdir+MrUiXy01S732GsDe8favW+6NkWTlBUmWE1IxWUx4HdoYN3ZT3Dh9bJYheF8qi6Depw2k/oyK8K+QNmi+/LA6ZmDxA==",
    "id": 7
},
{
    "domain": ".nike.com",
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "geoloc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "true",
    "storeId": "0",
    "value": "cc=KR,rc=,tp=vhigh,tz=GMT+9,la=37.57,lo=127.00",
    "id": 8
},
{
    "domain": ".nike.com",
    "expirationDate": 1627620900,
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "nike1_CID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "4b9644b5dda44438ee5bbeb2cfa1dcf3",
    "id": 9
},
{
    "domain": ".nike.com",
    "expirationDate": 1627620901.224158,
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "s_ecid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "MCMID%7C10223119284961012873355719364343489608",
    "id": 10
},
{
    "domain": ".nike.com",
    "expirationDate": 1879908901,
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "wa_pcid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "Iex1l1rNgSTHXBAFt9VjI",
    "id": 11
},
{
    "domain": ".nike.com",
    "expirationDate": 1879908901,
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "wa_randnum",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "156454890182373471387",
    "id": 12
},
{
    "domain": ".nike.com",
    "expirationDate": 1564678344,
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "wa_sid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "1564676536891-Iex1l1rNgSTHXBAFt9VjI",
    "id": 13
},
{
    "domain": "www.nike.com",
    "hostOnly": "true",
    "httpOnly": "true",
    "name": "ActiveID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "true",
    "session": "true",
    "storeId": "0",
    "value": "V04A-D2CN-IN69-RECV-BM94-ORM6-TBPR-IXU2",
    "id": 14
},
{
    "domain": "www.nike.com",
    "expirationDate": 1565281344.100058,
    "hostOnly": "true",
    "httpOnly": "false",
    "name": "AWSALB",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "dwYosyLd+DL5KCWm8xMVb0uaCGtaye+CBP7DmmpRzTQNAOjCnBlUhn++z72YncjUlSv+7/0TFSDSWyaD1Z29N85JlZQ/6WqZZLJo2MY9DuW2zEzwqBssCUd5qIy6",
    "id": 15
},
{
    "domain": "www.nike.com",
    "expirationDate": 1565153903,
    "hostOnly": "true",
    "httpOnly": "false",
    "name": "G_mouse_right_click",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "Y",
    "id": 16
},
{
    "domain": "www.nike.com",
    "hostOnly": "true",
    "httpOnly": "true",
    "name": "JSESSIONIDSITE",
    "path": "/kr/",
    "sameSite": "no_restriction",
    "secure": "true",
    "session": "true",
    "storeId": "0",
    "value": "71EC3A8F2841B0BA3DEA4EF2E1C38EAF.nike-site",
    "id": 17
},
{
    "domain": "www.nike.com",
    "hostOnly": "true",
    "httpOnly": "false",
    "name": "NikeCookie",
    "path": "/kr/ko_kr/t/men/fw/nike-sportswear/AT0298-100/gbmc26",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "true",
    "storeId": "0",
    "value": "ok",
    "id": 18
},
{
    "domain": "www.nike.com",
    "hostOnly": "true",
    "httpOnly": "false",
    "name": "social_type",
    "path": "/kr/ko_kr/t/men/fw/nike-sportswear/AT0298-100/gbmc26",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "true",
    "storeId": "0",
    "value": "social_facebook",
    "id": 19
},
{
    "domain": "www.nike.com",
    "hostOnly": "true",
    "httpOnly": "false",
    "name": "USERID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "true",
    "storeId": "0",
    "value": "134414933",
    "id": 20
},
{
    "domain": "www.nike.com",
    "expirationDate": 3712032547.420175,
    "hostOnly": "true",
    "httpOnly": "false",
    "name": "WHATAP",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "x36jqkfjbf9h46",
    "id": 21
}
]

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
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os, time

load_dotenv()

USER = os.environ["LOGIN_USER"]
PASS = os.environ["LOGIN_PASS"]
FAV_USER_ID = 32
SNS_URL = "https://uta.pw/sakusibbs/"

options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

url_login = SNS_URL + "users.php?action=login"
browser.get(url_login)
print("ログインページにアクセスしました")

# send post data
def form_post(frm, d):
    for field, value in d.items():
        e = frm.find_element_by_name(field)
        e.clear()
        e.send_keys(value)
    frm.submit()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".islogin")
        )
    )

frm = browser.find_element_by_css_selector("#loginForm form")
form_post(frm, {
    "username_mmlbbs6": USER,
    "password_mmlbbs6": PASS})

browser.save_screenshot("ssn-logined.png") #画像でログインチェック

#domでログインチェック
e = browser.find_element_by_id("bbsheader")
html = e.get_attribute("innerHTML")
if html.find("action=logout") < 0:
    print("ログイン失敗")
    quit()
print("+ ログインしました")
time.sleep(1)

# 作品一覧を開く
url = SNS_URL + "users.php?user_id=" + str(FAV_USER_ID)
browser.get(url)
print("作品一覧にアクセス")

# 作品一覧の取得
url_list = []
ul = browser.find_element_by_css_selector("#mmlist")
li_list = ul.find_elements_by_css_selector("li")
for li in li_list:
    a = li.find_element_by_css_selector("a")
    url = a.get_attribute('href') #post.php?mml_id=xxx
    title = a.text
    url_list.append((title, url))
print("+ 作品の一覧を {0} 件取得しました".format(len(url_list)))

#お気に入りをつける
#post.php?action=addfav&mml_id=664
for title, href in url_list:
    print("- ", title)
    browser.get(href)

    try:
        e = browser.find_element_by_id("fav_add_btn")
        e.click()

        print("| add this uta to your fav")
    except:
        print("| already this uta is your fav")
        e = browser.find_element_by_id("fav_remove_btn")
        e.click()
        print("| dell from your fav")

    time.sleep(1)
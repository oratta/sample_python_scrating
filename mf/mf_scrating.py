from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, os
from dotenv import load_dotenv
import setting

USER = os.environ["USER_NAME"]
PASS = os.environ["PASSWORD"]

# to get firefox's WebDriver
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

# access to login page
url_login = "https://moneyforward.com/users/sign_in"
browser.get(url_login)
print("success to access")

# input textbox
e = browser.find_element_by_css_selector("#sign_in_session_service_email")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_css_selector("#sign_in_session_service_password")
e.clear()
e.send_keys(PASS)
print("fill login info")

time.sleep(1)

# send form
frm = browser.find_element_by_css_selector("#login-btn-sumit")
frm.submit()
print("send login information")

# wait for reload
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.menu-item:nth-child(3) > a:nth-child(1)")))

# access to visitor log
url_visitor_log = "https://moneyforward.com/bs/portfolio"
browser.get(url_visitor_log)

total = browser.find_element_by_css_selector(".heading-radius-box")
print(total)

detDepoTable = browser.find_elements_by_css_selector("table.table:nth-child(2) > tbody > tr")
#detEquityTable = browser.find_element_by_css_selector(".table-eq")
#detMfTable = browser.find_element_by_css_selector(".table-mf")
#detOtherTable = browser.find_element_by_css_selector("#portfolio_det_oth > table:nth-child(3)")
#detPointTable = browser.find_element_by_css_selector("#portfolio_det_po > table:nth-child(3)")

#portfolio_det_bd > table > tbody > tr:nth-child(1)
SECTION_INFO = setting.SECTION_INFO

csv_array = []
section_tag = 'cash'
for tr in detDepoTable:
    row_array = {}
    td_list = tr.find_elements_by_css_selector("td")
    tr_id = 1
    for td in td_list:
        if tr_id == SECTION_INFO[section_tag]['name_tr_id']:
            row_array['name'] = td.text
        elif tr_id == SECTION_INFO[section_tag]['value_tr_id']:
            row_array['value'] = td.text
        elif tr_id == SECTION_INFO[section_tag]['belongs_tr_id']:
            row_array['belongs'] = td.text
        # print(td.text)
        tr_id += 1
    print(row_array)
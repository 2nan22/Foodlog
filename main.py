from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time
import json
import sqlite3
import utils.common_variables as common_variables
import scraping.common_variables as scraping_variables
import sqlite.common_variables as sqlite_variables

# 네이버 로그인 정보
STR_NAVER_ID = scraping_variables.STR_NAVER_ID
STR_NAVER_PASSWORD = scraping_variables.STR_NAVER_PASSWORD
# 경로
STR_PATH_DB = common_variables.STR_PATH_DB
STR_PATH_CHROMEDRIVER = common_variables.STR_PATH_CHROMEDRIVER

STR_CREATE_PLACE = sqlite_variables.STR_CREATE_TABLE_PLACE
STR_CREATE_EVALUATE = sqlite_variables.STR_CREATE_TABLE_EVALUATE
STR_INSERT_PLACE = sqlite_variables.STR_INSERT_PLACE
STR_INSERT_EVALUATE = sqlite_variables.STR_INSERT_EVALUATE

# 웹 드라이버 생성 및 네이버 로그인 페이지 이동
driver = webdriver.Chrome(STR_PATH_CHROMEDRIVER)
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(2)

# 아이디, 비밀번호 입력 후 로그인 버튼 클릭
id = driver.find_element(By.ID, 'id').send_keys(STR_NAVER_ID)
pwd = driver.find_element(By.ID, 'pw').send_keys(STR_NAVER_PASSWORD)
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'btn_login').click()

#TODO: 로그인 시, 자동입력문자 창이 뜰 경우 stop하고 입력 시까지 무한 대기하기

time.sleep(15)

# 내 장소 정보가 들어있는 페이지 이동
driver.get('https://map.naver.com/v5/api/bookmark/sync')

time.sleep(3)

# 내 장소 정보를 JSON 형태로 가져옴
bookmark_json = driver.find_element(By.XPATH, '/html/body/pre').text
bookmark_data = json.loads(bookmark_json)

# DB 연결 및 내 장소 정보 저장
conn = sqlite3.connect(STR_PATH_DB)
cur = conn.cursor()
conn.execute(STR_CREATE_PLACE)
conn.execute(STR_CREATE_EVALUATE)

dict_folder = {}

for item in tqdm(bookmark_data['my']['folderSync']['folders']):
    folder_id = item['folderId']
    folder_name = item['name']
    dict_folder[folder_id] = folder_name
    cnt = item['bookmarkCount']
    cur.execute(STR_INSERT_EVALUATE, 
                (folder_id, folder_name, cnt))

for item in tqdm(bookmark_data['my']['bookmarkSync']['bookmarks']):
    info = item['bookmark']

    store_name = info['name']
    store_nickname = info['displayName']
    latitude = info['py']
    longitude = info['px']
    create_time = info['creationTime']
    last_update_time = info['lastUpdateTime']
    address = info['address']
    memo = info['memo']
    if memo == '':
        memo = '-'
    place_type_id = info['mcid']
    place_type = info['mcidName']

    folder_info = item['folderMappings'][0]

    folder_id = folder_info['folderId']
    folder_name = dict_folder[folder_id]

    cur.execute(STR_INSERT_PLACE, 
                (store_name, store_nickname, address, memo, place_type_id, 
                 place_type, latitude, longitude, create_time, last_update_time, folder_id, folder_name))


conn.commit()
conn.close()

# 웹 드라이버 종료
driver.quit()

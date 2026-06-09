from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
df_titles = pd.DataFrame()
options = ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('headless')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

for k in range(0, 6):
    url = 'https://news.naver.com/section/10{}'.format(k)
    driver.get(url)

    div_num = 5 if k == 1 else 4  # 경제(k=1)만 div[5], 나머지는 div[4]

    button_xpath = '//*[@id="newsct"]/div[{}]/div/div[2]/a'.format(div_num)
    for i in range(30):
        driver.find_element(By.XPATH, button_xpath).click()
        time.sleep(0.5)
    titles = []
    for i in range(1, 180):
        for j in range(1, 7):
            try:
                title_xpath = '//*[@id="newsct"]/div[{}]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(
                    div_num, i, j)
                title = driver.find_element(By.XPATH, title_xpath).text
                print(title)
                titles.append(title)
            except:
                print('error', i, j)
    print(titles)
    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[k]
    df_titles = pd.concat(
        [df_titles, df_section_titles],
        ignore_index=True
    )
    print(df_titles.head())
    df_titles.info()
    df_titles.to_csv(
        './data/naver_news_section_{}.csv'.format(
            datetime.datetime.now().strftime('%Y%m%d')
        ),
        index=False
    )
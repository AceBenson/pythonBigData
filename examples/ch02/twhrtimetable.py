from selenium import webdriver
# 高鐵時刻表查詢網站
url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
ss='台中站'      #出發站
es='台北站'      #到達站
dd='2020/03/26' #日期 
dt='09:00'      #時間
# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
#輸入出發站
driver.find_element_by_id('StartStation').send_keys(ss) 
#輸入到達站
driver.find_element_by_id('EndStation').send_keys(es)   
#輸入日期
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id('DepartueSearchDate').send_keys(dd) 
#輸入時間
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id('DepartueSearchTime').send_keys(dt)
driver.find_element_by_id('SearchButton').click() #按查詢鈕
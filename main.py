# import time
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://tomsk.hh.ru/vacancies/programmist")
#
# time.sleep(3)
#
# vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-info--umZA61PpMY07JVJtomBA")
#
# parsed_data = []
#
# for vacancy in vacancies:
#     try:
#         title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-2').text
#         company = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___tkzIl_4-3-2").text
#         salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-15').text
#         link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-2').get_attribute('href')
#     except:
#         print("Произошла ошибка при парсинге")
#         continue
#
#     parsed_data.append([title, company, salary, link])
#
# driver.quit()
#
# with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
#     writer.writerows(parsed_data)








# data = [
#     ['100', '200', '300'],
#     ['400', '500', '600'],
#
#     ]
#
# numbers = []
#
# for row in data:
#     for text in row:
#         number = int(text)
#         numbers.append(number)
#
# print(numbers)



# import requests
# from bs4 import BeautifulSoup
#
# url = "https://"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
# rows = soup.find_all("tr")
# data = []
#
# for row in rows:
#     cols = row.find_all("td")
#     cleaned_cols = [col.text.strip() for col in cols]
#     data.append(cleaned_cols)
#
# print(data)

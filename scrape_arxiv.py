from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import pickle
from time import sleep

driver = webdriver.Firefox()
driver.get("https://arxiv.org/list/cond-mat.mtrl-sci/pastweek?show=144")
elems = driver.find_elements(By.CLASS_NAME, 'list-title')
# elems = driver.find_elements(By.LINK_TEXT, '')
article_titles = []
# article_abstracts = []
for elem in elems:
    article_titles.append(elem.text)
# print(article_titles)
print(len(article_titles))
# link_elems = driver.find_elements(By.XPATH, "//a[@href]")
# links = []
# for link_elem in tqdm(link_elems):
#     links.append(link_elem.get_attribute("href"))
# print(len(links))
# for link in tqdm(links):
#     if 'https://arxiv.org/abs/' in link:
#         # print(elem.get_attribute("href"))
#         driver.get(link_elem.get_attribute("href"))
#         sleep(2)
#         title_elem = driver.find_element(By.CLASS_NAME, 'title')
#         article_titles.append(title_elem.text)
#         abstract_elem = driver.find_element(By.CLASS_NAME, 'abstract')
#         article_abstracts.append(abstract_elem.text)
# print(len(article_titles))
# print(len(article_abstracts))
driver.get("https://en.wikipedia.org/wiki/Sheet_metal")
elems = driver.find_elements(By.TAG_NAME, 'body')
ml_wiki_texts = []
for elem in elems:
    ml_wiki_texts.append(elem.text)
print(len(ml_wiki_texts))
with open('article_titles.pkl', 'wb') as doc:
    pickle.dump(article_titles, doc)
with open('ml_wiki.pkl', 'wb') as doc:
    pickle.dump(ml_wiki_texts, doc)
driver.close()




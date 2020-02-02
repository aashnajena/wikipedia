import wikipedia as wk
import json
from tqdm import tqdm, tnrange
from time import sleep
import csv
import re

dic = {}
summary_dic = {}


f = open('./animals.txt','r')


pbar = tqdm(total = 383)
count_animal = 1
# length = 0
with open("animalsOutput.csv", "w") as csvFile:
	csvWriter = csv.writer(csvFile)
	for animal in f.readlines():
		# print(animal)
		animal = animal.lower().strip("\n")
		try:
			wiki_page= wk.WikipediaPage(title=animal)
			content = wiki_page.content
			content = content.strip()
			content = content.replace("\n", "")
			content = content.replace("=", "")
			# print(content)
			length = len(content.split())
			if length>1000:
				lt = [1, content]
				csvWriter.writerow(lt)
			pbar.update(1)
			# print(summary_dic)
		except:
			pass
pbar.close()


import wikipediaapi 
import wikipedia as wk
import json
from tqdm import tqdm, tnrange
from time import sleep

dic = {}
summary_dic = {}


f = open('./animals.txt','r')
animals = []
wiki_wiki = wikipediaapi.Wikipedia('en')

def findSubsections(s, section_number, section_list):
	for sub in s.sections:
		section_list[section_number].append(sub.title)
		findSubsections(sub, section_number, section_list)

def get_sections(sections):
	section_list = []
	section_number = 0
	for s in sections:
		empty_list = []
		empty_list.append(s.title)
		section_list.append(empty_list)

		findSubsections(s, section_number, section_list)
	return section_list	

def addDict(output_list, count_animal, wiki_page):
	section_number = 0
	for section in output_list:
		section_number +=1
		para_number = 1
		for subsection in section:
			paras = wiki_page.section(subsection).split("\n")
			for para in paras:
				key = "1_{}_{}_{}".format(count_animal,section_number,para_number)
				dic[key] = para
				para_number+=1
				

pbar = tqdm(total = 383)
count_animal = 1
length = 0
for animal in f.readlines():
	# print(animal)
	animal = animal.lower().strip("\n")
	try:
		page_py = wiki_wiki.page(animal)
		wiki_page= wk.WikipediaPage(title=animal)
		# print(len(wiki_page.content.split()))
		length += len(wiki_page.content.split())
		# summary_dic[count_animal] = wiki_page.summary
		# output_list = get_sections(page_py.sections)
		# # print(output_list)
		# addDict(output_list, count_animal,wiki_page)
		# count_animal = count_animal + 1
		pbar.update(1)
		# print(summary_dic)
	except:
		pass
pbar.close()

# with open("output_data.json","w") as f:
# 	json.dump(dic,f)		   

# with open("output_summary.json","w") as e:
# 	json.dump(summary_dic,e)	


print(length)
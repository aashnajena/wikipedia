import wikipediaapi
import wikipedia as wk
import json
from tqdm import tqdm, tnrange
from time import sleep

dic = {}
summary_dic = {}


f = open('./lang3.txt', 'r')
langs = []
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


def addDict(output_list, count_lang, wiki_page):
	section_number = 0
	for section in output_list:
		section_number += 1
		para_number = 1
		for subsection in section:
			paras = wiki_page.section(subsection).split("\n")
			for para in paras:
				key = "1_{}_{}_{}".format(count_lang, section_number, para_number)
				dic[key] = para
				para_number += 1


pbar = tqdm(total=400)
count_lang = 1
list_true = []
for lang in f.readlines():
    # print(lang)
    lang = lang.strip("\n")
    try:
        page_py = wiki_wiki.page(lang)
        wiki_page= wk.WikipediaPage(title=lang)
        length_avg = int(1000)
        if len(wiki_page.content.split()) >= length_avg :
            list_true.append(lang)
            summary_dic[count_lang] = wiki_page.summary
            output_list = get_sections(page_py.sections)
            # print(output_list)
            addDict(output_list, count_lang,wiki_page)
            count_lang = count_lang + 1
        else:
            pass
    except:
        # print("error", lang)
        pass
    pbar.update(1)

	# print(summary_dic)
pbar.close()

with open("output_data_lang.json","w") as f:
	json.dump(dic,f)		   

with open("output_summary_lang.json","w") as e:
	json.dump(summary_dic,e)	

print(len(list_true),list_true)


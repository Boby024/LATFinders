import json

import requests as requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    categories = []
    courses = json.load(open('courses.json'))["courses"]

    for course in courses:
        cid = course["id"]
        link = course["identityLink"]
        category = None
        subCategory = None
        subSubCategory = None
        print("Currently scraping course with ID " + str(cid))

        review_page = requests.get(link, headers={'User-agent': 'your bot 0.1'})
        review_soup = BeautifulSoup(review_page.content, "html.parser")
        ol = review_soup.find("ol", class_="breadcrumb")
        if ol:
            lis = ol.find_all("li")
            if not (len(lis) == 6):
                print("Warning!")
                print("something is out of the ordinary on " + link)
            else:
                category = lis[2].find("span").text
                subCategory = lis[3].find("span").text
                subSubCategory = lis[4].find("span").text

        categories.append({
            'course_id': cid,
            'course_link': link,
            'category': category,
            'subCategory': subCategory,
            'subSubCategory': subSubCategory
        })

    with open("categories.json", "w") as outfile:
        outfile.write(json.dumps({"categories": categories}, indent=2, ensure_ascii=False))
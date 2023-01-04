import json

import requests
from bs4 import BeautifulSoup

id_counter = 0
academies_dictionary = {
    "institutes": []
}


def parse_academy_info(inst):
    institute_title_link = inst.find("a", class_="institute-title-link")
    institute_title = institute_title_link.text
    institute_link = institute_title_link["href"]
    institute_type = " ".join(inst.find("div", class_="institute-type").text.split())
    institute_course_count = int(inst.find("div", class_="course-count").text.split()[:-1].pop())
    inst_feedback_arr = inst.find_all("div", class_="tooltip-content__rating-value")

    # institute_overall_rating = None
    # institute_review_count = 0
    # institute_recommendation_rate = None
    institute_score = None

    # institute_course_contents_rating = None
    # institute_docents_rating = None
    # institute_lectures_rating = None
    # institute_furnishings_rating = None
    # institute_organization_rating = None
    # institute_library_rating = None
    # institute_digitization_rating = None

    # Some entries like "Akademie Würth Business School" have not a single rating
    # if len(inst_feedback_arr) > 1:
    # institute_overall_rating = float(inst_feedback_arr[0].text)
    # institute_review_count = int(inst_feedback_arr[2].text)
    # institute_recommendation_rate = inst_feedback_arr[1].text

    # Some entries like "ADK Baden-Württemberg" have no calculated score
    if len(inst_feedback_arr) > 3:
        institute_score = inst_feedback_arr[3].text.strip()

    additional_info_page = requests.get(institute_link, headers={'User-agent': 'your bot 0.1'})
    additional_info_soup = BeautifulSoup(additional_info_page.content, "html.parser")
    institute_facts = additional_info_soup.find("dl", class_="institute-facts")
    # detailed_rating = additional_info_soup.find("ul", class_="report-criteria-list")

    institute_student_count = institute_facts.find("dt", string="Studierende")
    institute_docent_count = institute_facts.find("dt", string="Dozenten")
    institute_professor_count = institute_facts.find("dt", string="Professoren")
    institute_year_of_foundation = institute_facts.find("dt", string="Gründung")

    if institute_student_count:
        institute_student_count = int(
            institute_student_count.find_next_sibling().text.split("Studierende")[0].strip().replace(".", ""))

    if institute_docent_count:
        institute_docent_count = int(
            institute_docent_count.find_next_sibling().text.split("Dozenten")[0].strip().replace(".", ""))

    if institute_professor_count:
        institute_professor_count = int(
            institute_professor_count.find_next_sibling().text.split("Professoren")[0].strip().replace(".", ""))

    if institute_year_of_foundation:
        institute_year_of_foundation = int(
            institute_year_of_foundation.find_next_sibling().text.split("Gründungsjahr")[1].strip())

    # if detailed_rating:
    # institute_course_contents_rating = float(detailed_rating
    # .find("span", string="Studieninhalte").find_next_sibling()
    # .find("div", class_="rating-value").text.strip())

    # institute_docents_rating = float(detailed_rating
    # .find("span", string="Dozenten").find_next_sibling()
    # .find("div", class_="rating-value").text.strip())

    # institute_lectures_rating = float(detailed_rating
    # .find("span", string="Lehrveranstaltungen").find_next_sibling()
    # .find("div", class_="rating-value").text.strip())

    # institute_furnishings_rating = float(detailed_rating
    # .find("span", string="Ausstattung").find_next_sibling()
    # .find("div", class_="rating-value").text.strip())

    # institute_organization_rating = float(detailed_rating
    # .find("span", string="Organisation").find_next_sibling()
    # .find("div", class_="rating-value").text.strip())

    # institute_library_rating = detailed_rating.find("span", string="Bibliothek")
    # institute_digitization_rating = detailed_rating.find("span", string="Digitales Studieren")

    # "Bibliothek" and "Digitales Studieren" are optional: https://www.studycheck.de/bewerten
    # if institute_library_rating:
    # institute_library_rating = float(
    # institute_library_rating.find_next_sibling().find("div", class_="rating-value").text.strip())

    # if institute_digitization_rating:
    # institute_digitization_rating = float(
    # institute_digitization_rating.find_next_sibling().find("div", class_="rating-value").text.strip())

    # rating_distribution = additional_info_soup.find("div",class_="js-rating-filter").find_all("div",
    # class_="report-count")

    # institute_review_count_1_star = int(rating_distribution[4].text.strip())
    # institute_review_count_2_star = int(rating_distribution[3].text.strip())
    # institute_review_count_3_star = int(rating_distribution[2].text.strip())
    # institute_review_count_4_star = int(rating_distribution[1].text.strip())
    # institute_review_count_5_star = int(rating_distribution[0].text.strip())

    global id_counter
    id_counter += 1

    inst_dict = {'id': id_counter,
                 'name': institute_title,
                 'type': institute_type,
                 'numberOfCourses': institute_course_count,
                 # 'overallRating': institute_overall_rating,
                 # 'numberOfReviews': institute_review_count,
                 # 'recommendationRate': institute_recommendation_rate,
                 'score': institute_score,
                 # 'courseContentsRating': institute_course_contents_rating,
                 # 'docentsRating': institute_docents_rating,
                 # 'lecturesRating': institute_lectures_rating,
                 # 'furnishingsRating': institute_furnishings_rating,
                 # 'organizationRating': institute_organization_rating,
                 # 'libraryRating': institute_library_rating,
                 # 'digitizationRating': institute_digitization_rating,
                 # 'numberOf1StarReviews': institute_review_count_1_star,
                 # 'numberOf2StarReviews': institute_review_count_2_star,
                 # 'numberOf3StarReviews': institute_review_count_3_star,
                 # 'numberOf4StarReviews': institute_review_count_4_star,
                 # 'numberOf5StarReviews': institute_review_count_5_star,
                 'identityLink': institute_link,
                 'yearOfFoundation': institute_year_of_foundation,
                 'numberOfStudents': institute_student_count,
                 'numberOfDocents': institute_docent_count,
                 'numberOfProfessors': institute_professor_count}

    academies_dictionary.get("institutes").append(inst_dict)


def scrape_page(num):
    link = ("https://www.studycheck.de/hochschulen/seite-" + "%d" + "?o=4") % num

    # Returns a "Too Many Requests" (429) error when user agent is not set
    page = requests.get(link, headers={'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(page.content, "html.parser")

    for institute in soup.find_all("div", class_="institute-item"):
        parse_academy_info(institute)


if __name__ == '__main__':
    # 25 pages in total - upper limit is excluded
    print("Getting started...")

    for x in range(1, 26):
        scrape_page(x)
        print("Progress: " + str(4 * x) + "%")

    with open("academies.json", "w") as outfile:
        outfile.write(json.dumps(academies_dictionary, indent=2))

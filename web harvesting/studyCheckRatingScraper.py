import json

import requests as requests
from bs4 import BeautifulSoup


def find_amount_stars(ratings_arr):
    # from worst to best
    return [sum(1 for r in ratings_arr if r["overallRating"] < 2.0),
            sum(1 for r in ratings_arr if 3.0 > r["overallRating"] >= 2.0),
            sum(1 for r in ratings_arr if 4.0 > r["overallRating"] >= 3.0),
            sum(1 for r in ratings_arr if 5.0 > r["overallRating"] >= 4.0),
            sum(1 for r in ratings_arr if r["overallRating"] == 5.0)]


def calculate_average_ratings(ratings_arr):
    library_ratings = list(filter(lambda i: i["libraryRating"], ratings_arr))
    digitization_ratings = list(filter(lambda i: i["digitizationRating"], ratings_arr))
    nof_lib_ratings = len(library_ratings)
    nof_digi_ratings = len(digitization_ratings)

    course_contents_ratings_sum = sum(map(lambda i: i["courseContentsRating"], ratings_arr))
    docents_ratings_sum = sum(map(lambda i: i["docentsRating"], ratings_arr))
    lectures_ratings_sum = sum(map(lambda i: i["lecturesRating"], ratings_arr))
    furnishings_ratings_sum = sum(map(lambda i: i["furnishingsRating"], ratings_arr))
    organization_ratings_sum = sum(map(lambda i: i["organizationRating"], ratings_arr))
    library_ratings_sum = sum(map(lambda i: i["libraryRating"], library_ratings))
    digitization_ratings_sum = sum(map(lambda i: i["digitizationRating"], digitization_ratings))
    overall_ratings_sum = sum(map(lambda i: i["overallRating"], ratings_arr))

    return {
        'courseContents': (course_contents_ratings_sum / len(ratings_arr)) if len(ratings_arr) else None,
        'docents': (docents_ratings_sum / len(ratings_arr)) if len(ratings_arr) else None,
        'lectures': (lectures_ratings_sum / len(ratings_arr)) if len(ratings_arr) else None,
        'furnishings': (furnishings_ratings_sum / len(ratings_arr)) if len(ratings_arr) else None,
        'organization': (organization_ratings_sum / len(ratings_arr)) if len(ratings_arr) else None,
        'library': (library_ratings_sum / nof_lib_ratings) if nof_lib_ratings else None,
        'digitization': (digitization_ratings_sum / nof_digi_ratings) if nof_digi_ratings else None,
        'overall': (overall_ratings_sum / len(ratings_arr)) if len(ratings_arr) else None,
    }


def update_rating_summary(item_to_change, ratings_arr):
    average_ratings = calculate_average_ratings(ratings_arr)
    rating_distribution = find_amount_stars(ratings_arr)
    nof_reviews = sum(rating_distribution)
    nof_recommendations = sum(map(lambda i: i["reviewRecommendation"], ratings_arr))
    recommendation_rate = nof_recommendations / nof_reviews if nof_reviews else None
    item_to_change["courseContentsRating"] = average_ratings["courseContents"]
    item_to_change["docentsRating"] = average_ratings["docents"]
    item_to_change["lecturesRating"] = average_ratings["lectures"]
    item_to_change["furnishingsRating"] = average_ratings["furnishings"]
    item_to_change["organizationRating"] = average_ratings["organization"]
    item_to_change["libraryRating"] = average_ratings["library"]
    item_to_change["digitizationRating"] = average_ratings["digitization"]
    item_to_change["overallRating"] = average_ratings["overall"]
    item_to_change["numberOf1StarReviews"] = rating_distribution[0]
    item_to_change["numberOf2StarReviews"] = rating_distribution[1]
    item_to_change["numberOf3StarReviews"] = rating_distribution[2]
    item_to_change["numberOf4StarReviews"] = rating_distribution[3]
    item_to_change["numberOf5StarReviews"] = rating_distribution[4]
    item_to_change["numberOfReviews"] = nof_reviews
    item_to_change["recommendationRate"] = recommendation_rate


def write_json(obj, filename):
    with open(filename + ".json", "w") as outfile:
        outfile.write(json.dumps(obj, indent=2))


if __name__ == '__main__':
    ratings_dictionary = {"ratings": []}
    id_counter = 0
    academies_json = json.load(open('academies.json'))
    courses_json = json.load(open('courses.json'))
    print("Getting started...")

    for academy_id in range(1, 600):
        ratings = []

        for institute in filter(lambda i: i["id"] == academy_id, academies_json["institutes"]):
            academy_name = institute["name"]
            print("Scraping Academy '" + academy_name + "' with ID " + str(academy_id))

            review_urls = []

            # The uni with the most reviews has a maximum of 2316 review pages
            for x in range(1, 2317):

                link = institute["identityLink"] + "/bewertungen/seite-" + str(x)
                print(str(x) + " Pages found...")
                page = requests.get(link, headers={'User-agent': 'your bot 0.1'})
                soup = BeautifulSoup(page.content, "html.parser")
                if "Seite nicht gefunden (404)" in soup.find("title").text:
                    break
                else:
                    reports = soup.findAll("div", class_="report-item-boxed")
                    for report in reports:
                        review_urls.append(report.find("h3").find("a")["href"])

            for index, review_url in enumerate(review_urls):
                print(str(index + 1) + " / " + str(len(review_urls)) + " " + review_url)
                review_page = requests.get(review_url, headers={'User-agent': 'your bot 0.1'})
                review_soup = BeautifulSoup(review_page.content, "html.parser")
                author_info = review_soup.find("div", class_="reports-authorinfo")
                author_name = author_info.find("h2").text.split("Über ")[1]

                author_age = None
                author_gender = None
                author_form_of_study = None
                author_study_status = None
                author_current_semester = None
                author_year_of_study_start = None
                author_school_leaving_qualification = None
                author_gpa = None

                review_recommendation = None
                review_day_of_creation = None
                review_day_of_publication = None
                review_views = None

                rating_course_contents = None
                rating_docents = None
                rating_lectures = None
                rating_furnishings = None
                rating_organization = None
                rating_library = None
                rating_digitization = None
                rating_overall = None

                lis = author_info.find("ul", class_="list-unstyled").findAll("li")

                for li in lis:
                    keyValuePair = li.text.strip().split(": ")

                    if keyValuePair[0] == "Alter":
                        author_age = keyValuePair[1].replace("Über 35", ">35").replace("Unter 18", "<18")

                    elif keyValuePair[0] == "Geschlecht":
                        author_gender = keyValuePair[1] \
                            .replace("Männlich", "M").replace("Weiblich", "F").replace("Divers", "X")

                    elif keyValuePair[0] == "Studienform":
                        author_form_of_study = keyValuePair[1]

                    elif keyValuePair[0] == "Abschluss":
                        author_study_status = keyValuePair[1]

                        if author_study_status == "Ja":
                            author_study_status = "Finished"
                        elif author_study_status == "Ich studiere noch":
                            author_study_status = "Work in progress"
                        else:
                            author_study_status = "Cancelled"

                    elif keyValuePair[0] == "Aktuelles Fachsemester":
                        author_current_semester = int(keyValuePair[1])

                    elif keyValuePair[0] == "Studienbeginn":
                        author_year_of_study_start = int(keyValuePair[1])

                    elif keyValuePair[0] == "Schulabschluss":
                        author_school_leaving_qualification = keyValuePair[1]

                    elif keyValuePair[0] == "Abischnitt":
                        author_gpa = float(keyValuePair[1].replace(",", "."))

                    elif keyValuePair[0] == "Weiterempfehlung":
                        review_recommendation = keyValuePair[1]
                        review_recommendation = True if review_recommendation == "Ja" else False

                    elif keyValuePair[0] == "Geschrieben am":
                        review_day_of_creation = keyValuePair[1]

                    elif keyValuePair[0] == "Veröffentlicht am":
                        review_day_of_publication = keyValuePair[1]

                review_header = review_soup.find("header", class_="card-header")

                course_identity_link = review_header.find("p").find("a")["href"]

                review_heading = review_header.find("h1").text

                rating_lis = review_soup.find("div", "report-ratings").find("ul").findAll("li")

                views = review_soup.find("div", "footer-right").find("span", class_="hint--top")
                if views:
                    parent = views.parent
                    if parent:
                        review_views = parent.text.strip()

                for rating_li in rating_lis:
                    rating_value = float(rating_li.find("div", class_="rating-value").text.strip())
                    rating_li.find("div", class_="item-rating").clear()
                    rating_key = rating_li.text.strip()

                    if rating_key == "Studieninhalte":
                        rating_course_contents = rating_value
                    elif rating_key == "Dozenten":
                        rating_docents = rating_value
                    elif rating_key == "Lehrveranstaltungen":
                        rating_lectures = rating_value
                    elif rating_key == "Ausstattung":
                        rating_furnishings = rating_value
                    elif rating_key == "Organisation":
                        rating_organization = rating_value
                    elif rating_key == "Bibliothek":
                        rating_library = rating_value
                    elif rating_key == "Digitales Studieren":
                        rating_digitization = rating_value
                    elif rating_key == "Gesamtbewertung":
                        rating_overall = rating_value

                course = list(filter(lambda i: i["identityLink"] == course_identity_link, courses_json["courses"]))
                course_id = course[0]["id"] if course else None
                course_name = course[0]["title"] if course else None

                ratings.append({
                    'id': 0,
                    'authorName': author_name,
                    'authorAge': author_age,
                    'authorGender': author_gender,
                    'authorFormOfStudy': author_form_of_study,
                    'authorStudyStatus': author_study_status,
                    'authorCurrentSemester': author_current_semester,
                    'authorYearOfStudyStart': author_year_of_study_start,
                    'authorSchoolLeavingQualification': author_school_leaving_qualification,
                    'authorGPA': author_gpa,
                    'reviewRecommendation': review_recommendation,
                    'reviewDayOfCreation': review_day_of_creation,
                    'reviewDayOfPublication': review_day_of_publication,
                    'reviewHeading': review_heading,
                    'reviewViews': review_views,
                    'courseContentsRating': rating_course_contents,
                    'docentsRating': rating_docents,
                    'lecturesRating': rating_lectures,
                    'furnishingsRating': rating_furnishings,
                    'organizationRating': rating_organization,
                    'libraryRating': rating_library,
                    'digitizationRating': rating_digitization,
                    'overallRating': rating_overall,
                    'identityLink': review_url,
                    'academyId': academy_id,
                    'academyName': academy_name,
                    'courseId': course_id,
                    'courseName': course_name,
                })

            update_rating_summary(institute, ratings)

        for c_id in range(1, 21000):
            course_ratings = list(filter(lambda i: i["courseId"] == c_id, ratings))
            if course_ratings:
                for item in filter(lambda i: i["id"] == c_id, courses_json["courses"]):
                    update_rating_summary(item, course_ratings)

        for rating in ratings:
            id_counter += 1
            rating["id"] = id_counter
            ratings_dictionary["ratings"].append(rating)

        print("Progress: " + str(academy_id * 0.17036)[:5] + " %\n")

    write_json(academies_json, "academies")
    write_json(courses_json, "courses")
    write_json(ratings_dictionary, "ratings")

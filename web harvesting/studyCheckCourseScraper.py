import json

import requests
from bs4 import BeautifulSoup

course_dictionary = {
    "courses": []
}


def scrape_page(num):
    link = ("https://www.studycheck.de/suche?rt=2&page=" + "%d") % num
    # Returns a "Too Many Requests" (429) error when user agent is not set
    page = requests.get(link, headers={'User-agent': 'your bot 0.1'})
    institutes = BeautifulSoup(page.content, "html.parser").find("div", class_="rfv1-card__content")

    for institute in institutes.find_all("div", class_="rfv1-media-layout__two-column-container"):
        # remove all ads, since they produce doublings
        if not (institute.find("span", class_="rfv1-label--absolute-top-right")):

            identity_link = institute.find("a", class_="rfv1-font-style--none")["href"]
            is_teacher_training = False
            academy_id = None
            academy_name = None

            soup = BeautifulSoup(requests.get(identity_link,
                                              headers={'User-agent': 'your bot 0.1'}).content, "html.parser")

            title = soup.find("span", class_="item-course-title")

            print(identity_link)

            ld_json = soup.find("script", type="application/ld+json")

            if title:
                title = title.text.replace("(Staatliche Prüfung und B.A.)", "")
            else:
                if ld_json:
                    title = json.loads(ld_json.text)["name"]
                else:
                    title = soup.find("div", "details-card")
                    if title:
                        title = title.find("div", "card-block").find("p").text.split('Das Studium "')
                        if len(title) == 1:
                            title = title[0].split('Die Ausbildung "')
                        title = title[1].split('" an der ')[0]
                    else:
                        title = soup.find("meta", property="og:description")["content"]
                        title = title.split("Das Studium ")[1].split(" beim Institut ")[0]

            if soup.find("h1", class_="course-title").find("span", string="Lehramt"):
                is_teacher_training = True

            degree_type = soup.find("div", string="Abschluss")

            if degree_type:
                degree_type = degree_type.find_next_sibling()

                small = degree_type.find("small")
                if small:
                    small.clear()

                degree_type = degree_type.text.strip()

            else:
                if ld_json:
                    degree_type = json.loads(ld_json.text)["educationalCredentialAwarded"]
                else:
                    degree_type = soup.find("title").text.split(") | ")[:-1][0].split(" (").pop()

            academy_info = soup.find("div", class_="institute-text")
            academy_link = academy_info.find("a")

            if academy_link:
                academy_link = academy_link["href"]
            else:
                academy_info = academy_info.text.strip()
                print("Warning! Institute '" + academy_info + "' could not be found in database.")

                # 5 institutes have no own profile page - Use their partner academy instead
                cooperation_unis = {
                    'Abo Akademi University': 'https://www.studycheck.de/hochschulen/uni-bielefeld',
                    'ADI - Akademie der Immobilienwirtschaft': 'https://www.studycheck.de/hochschulen/dhbw',
                    'Pädagogische Hochschule Thurgau': 'https://www.studycheck.de/hochschulen/uni-konstanz',
                    'TUM Asia': 'https://www.studycheck.de/hochschulen/tu-muenchen',
                    'Uni Straßburg': 'https://www.studycheck.de/hochschulen/uni-mainz'
                }

                academy_link = cooperation_unis.get(academy_info)

            for academy in json.load(open('academies.json'))["institutes"]:
                if academy["identityLink"] == academy_link:
                    academy_id = academy["id"]
                    academy_name = academy["name"]

            # rating = soup.find("div", "rating-value")
            # if rating:
            # rating = float(rating.text.strip())

            # recommendation_rate = soup.find("span", class_="recommendation")
            # if recommendation_rate:
            # recommendation_rate = recommendation_rate.text.split("\n")[0] + "%"

            # review_count = soup.find("div", "report-count")
            # if not review_count:
            # review_count = soup.find("span", "report-count")

            # review_count = int(review_count.text.strip()) if review_count else 0

            # if review_count == 0:
            # rating = None
            # recommendation_rate = None

            standard_period_of_study = institute.find("div", class_="rfv1-mt--s").find("span").text
            classroom_language = soup.findAll("div", class_="card-row-label")

            for cl in classroom_language:
                if cl.text.strip() == "Unterrichtssprachen":
                    classroom_language = cl.find_next_sibling().text.split(", ")
                    break

            course_dictionary.get("courses").append({
                'id': 0,
                'title': title,
                'academyName': academy_name,
                'academyId': academy_id,
                'degreeType': degree_type,
                'isTeacherTraining': is_teacher_training,
                'identityLink': identity_link,
                'standardPeriodOfStudy': standard_period_of_study,
                'classroomLanguages': classroom_language,
                # 'overallRating': None,
                # 'numberOfReviews': None,
                # 'recommendationRate': None,
            })


if __name__ == '__main__':
    print("Getting started...")
    # 2049 pages in total - upper limit is excluded
    for x in range(1, 2050):
        scrape_page(x)
        print("Page " + str(x) + " complete")
        print("Progress: " + str(0.0488 * x)[:5] + " %")

    course_dictionary['courses'] = sorted(course_dictionary['courses'], key=lambda k: k['title'])

    id_counter = 0
    for course in course_dictionary['courses']:
        id_counter += 1

        course['id'] = id_counter

    with open("courses.json", "w") as outfile:
        outfile.write(json.dumps(course_dictionary, indent=2))

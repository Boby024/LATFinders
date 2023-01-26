export interface Uni {
  id: number,
  name: string,
  type?: string,
  number_ofcourses?: number,
  identity_link?: string,
  year_of_foundation?: number,
  number_of_students?: number,
  number_of_docents?: number,
  number_of_professors?: number,
  score: number
}

export interface Course {
  id: number,
  course_name: string,
  uni_id: number,
  degree_type: string,
  is_teacher_training?: boolean,
  identity_link?: string,
  standard_period_of_study?: string,
  classroom_languages?: string
}

export interface Rating {
  id: number,
  course_id: number,
  date: number,
  author_name: number,
  author_current_semester: number,
  review_heading: number,
  author_school_leaving_qualification: number,
  author_gpa: number,
  author_year_of_study: number,
  author_age: number,
  furnishings_rating: number,
  author_form_of_study: number,
  course_contents_rating: number,
  library_rating: number,
  organization_rating: number,
  review_day_of_publication: number,
  author_study_status: number,
  review_recommendation: boolean,
  author_gender: number,
  review_day_of_creation: number,
  lectures_rating: number,
  digitization_rating: number,
  review_views : number,
  overall_rating: number,
  docents_rating: number,
  identity_link: number
}

export interface SearchQuery {
  id?: number,
  query?: string
}

export interface AnalyticQuery {
  uni_id?: number,
  course_id?: number,
  rating_gender?: string
}

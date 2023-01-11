export interface Uni {
  id: number,
  name: string
}

export interface Course {
  id: number,
  course_name: string,
  uni_id: number
}

export interface Rating {
  id: number,
  course_id: number,
  date: string,
  general_rating: number,
  rating_of_content: number,
  rating_of_professors: number,
  rating_of_lectures: number,
  rating_of_equipments: number,
  rating_of_Organisation: number,
  rating_of_library: number,
  rating_of_digital_studying: number,
  start_of_studies: number,
  suggest_to_others: number,
  gender: number,
  degree: number,
  age: number
}

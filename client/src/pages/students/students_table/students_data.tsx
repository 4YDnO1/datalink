import {
	Student
} from "./students_columns";

import students_data from "./students_data.json";

export function get_students_data(): Student[] {
	// Fetch data from your API here.
	return students_data;
}

export default get_students_data;
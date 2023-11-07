import {
	useState
} from "react";

import Table from "../../../components/table/table";

import {
	Student,
	students_columns
} from "./students_columns";

import {
	get_students_data
} from "./students_data";

import "./students_table.sass";


export function StudentsTable() {
	const students_data = get_students_data();
	const [data, /*setData*/] = useState<Student[]>(students_data);

	return (
		<>
			<Table columns={students_columns} data={data} />
		</>
	);
}

export default StudentsTable;
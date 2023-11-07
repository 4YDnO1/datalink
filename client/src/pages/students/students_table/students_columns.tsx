import {
	ColumnDef 
} from "@tanstack/react-table";

export type Student = {
	id: number;
	student_surname: string;
	student_firstname: string;
	student_patronymic: string;
	student_dob: number;
}

export const students_columns: ColumnDef<Student>[] =  [
	{
		accessorKey: "id",
		header: "Номер"
	},
	{
		accessorKey: "student_surname",
		header: "Фамилия"
	},
	{
		accessorKey: "student_firstname",
		header: "Имя"
	},
	{
		accessorKey: "student_patronymic",
		header: "Отчество"
	},
	{
		accessorKey: "student_dob",
		header: "Дата рождения (timestamp)"
	}
];

export default students_columns;
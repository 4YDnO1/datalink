import StudentsTable from "./students_table/students_table";

import "./students.sass";

export function Table() {
	return (
		<>
			<section className="section-wrapper">
				<div className="content-container">
					<div className="content flex flex-col py-[15px]">
						<h1>Table playground</h1>
					</div>
					<div className="content flex flex-col py-[15px]">
						<StudentsTable />
					</div>
				</div>
			</section>
		</>
	);
}
export default Table;

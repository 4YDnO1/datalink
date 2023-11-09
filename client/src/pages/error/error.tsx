import "./error.sass";

export default function Error() {
	document.title = "Error 404 | Datalink";
	return (
		<>
			<section className="section-wrapper">
				<div className="content-container">
					<div className="content flex flex-col py-[20px]">
						<h1>Ошибка 404, извините, страница не найдена</h1>
					</div>
				</div>
			</section>
		</>
	);
}
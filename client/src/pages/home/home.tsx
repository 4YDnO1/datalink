import { useEffect, useState, useCallback } from "react";
import "./home.sass";
import { Api } from '../../main'
import axios from 'axios';
import { ResponseType } from 'axios';
import {useStream} from 'react-fetch-streams';
import useWebSocket, { ReadyState, useSocketIO } from 'react-use-websocket';
import io from 'socket.io';
import loader from "../../../public/loader.gif";


export function Home() {
	const controller = new AbortController()

	const [question, setQuestion] = useState("");
	const [answerList, setAnswerList] = useState([]);
	const [isLoading, setLoading] = useState(false);

	const handleChange = (e) => setQuestion(e.target.value);

	const generateContent = async (answer: any) => {
		const URL = `http://127.0.0.1:5000/answer_question`
		const response = await fetch(URL, {
			method: "POST",

			headers: {
				'Content-Type': 'application/json;charset=utf-8'
			},

			body: JSON.stringify(answer)
		});

		const result = await response.json();

		setAnswerList(prevList => prevList.map(answer => {
			if (result.id == answer.id) {
			  return { ...answer, content: result.content };
			}
			return answer;
		}));
	}

	const processQuestion = async () => {
		if (question === "") {
			return;
		}

		const URL = `http://127.0.0.1:5000/get_questions`

		try {
			const response = await fetch(URL, {
				method: "POST",

				headers: {
					'Content-Type': 'application/json;charset=utf-8'
				},

				body: JSON.stringify({
					question: question
				})
			});

			if (!response.ok || !response.body) {
				throw response.statusText;
			}

			const reader = response.body.getReader();
			const decoder = new TextDecoder();

			while (true) {
				const { value, done } = await reader.read();

				if (done) {
					break;
				}

				const decodedChunk = decoder.decode(value, { stream: true });

				const JSONChunk = JSON.parse(decodedChunk);

				generateContent(JSONChunk);
				setAnswerList((prevList) => [...prevList, JSONChunk]);
			}

		} catch (error) {
			console.log(error)
		}
	};

	const onFormSubmit = async (e: any) => {
		e.preventDefault();

		setLoading(true);
		await processQuestion();
	}

	return (
		<>
			<section className="section-wrapper">
				<div className="content-container">
					<div className="w-[1000px] content flex flex-col py-[20px]">
						<div>
							<form action="" onSubmit={(e) => {
								e.preventDefault();
							}}>
								<div className="">
									<input className="appearance-none border-2 border-[#737373] rounded w-full py-2 px-4 text-white leading-tight focus:outline-none bg-[#27272a] focus:bg-[#3f3f46] focus:border-[#7D7C7C]" id="inline-password" type="text" placeholder="Тема для дата сета" value={question} onChange={handleChange} />
								</div>

								<div className=" mt-3 flex items-center">
									<button
										className='mr-2 px-3 py-2 rounded bg-[#0284c7] text-white text-black hover:bg-[#0ea5e9] transition-all' type="submit" onClick={(e) => onFormSubmit(e)}>
										Определить
									</button>
									{ !answerList.length && isLoading && <img className='w-[40px]' src={loader} alt="loader" /> }
								</div>
							</form>
						</div>
						<div className="mt-3">
							<h3 className="mb-2 font-semibold text-gray-900 dark:text-white">Полученные данные</h3>
							<ul className="text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-[#27272a] dark:border-[#737373] dark:text-white">
								{answerList.map((element) =>
									<li key={element.id} className="hover:bg-[#18181b] w-full px-4 py-4 border-b border-gray-200 rounded-lg dark:border-gray-600">
										<div className="flex items-center mb-2 gap-2">
											{ !element.content && <img className='w-[25px]' src={loader} alt="loader" /> }
											<label className="w-full text-sm font-medium text-gray-900 dark:text-gray-300">{element.question}</label>
										</div>
										<label className="font-normal">{element.content}</label>
									</li>
								)}
							</ul>
						</div>

					</div>
				</div>
			</section>
		</>
	);
}
export default Home;

import { Routes, Route } from "react-router-dom";

import Header from "../components/header/header";
import Footer from "../components/footer/footer";

import Home from "../pages/home/home";
import Error from "../pages/error/error";

import "./app.sass";

function App() {
	return (
		<>
			<Header />
			<main className="main-wrapper">
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/api" element={<Error />} />
					<Route path="*" element={<Error />} />
				</Routes>
			</main>
			<Footer />
		</>
	);
}

export default App;

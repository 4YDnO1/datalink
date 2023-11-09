// import React from "react";
import ReactDOM from "react-dom/client";
import {
	BrowserRouter
} from "react-router-dom";

import App from "./app/app.tsx";


export const Api = "http://127.0.0.1:8000/api/"

ReactDOM.createRoot(document.getElementById('app')!).render(
	// <React.StrictMode>
	<BrowserRouter>
		<App />
	</BrowserRouter>
	// </React.StrictMode>
);
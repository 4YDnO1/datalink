import  { NavLink } from "react-router-dom";

import "./header.sass";

function Header() {

	return (
		<header className="header-wrapper">
			<div className="content-container">
				<div className="content flex flex-wrap justify-center gap-2 py-4">

					{/* <div className="flex justify-center flex-wrap gap-2">
						<a href="https://vitejs.dev" target="_blank" rel="noreferrer">
							<img src="/assets/images/vite.svg" className="logo" alt="Vite logo" draggable="false" />
						</a>
						<a href="https://react.dev" target="_blank" rel="noreferrer">
							<img src="/assets/images/react.svg" className="logo" alt="React logo" draggable="false" />
						</a>
					</div> */}

					<nav className="flex items-center">
						<ul className="flex justify-center items-center flex-wrap gap-4">

							<li className="flex items-center">
								<NavLink to="/" className="flex justify-center items-center">
									home
								</NavLink>
							</li>
							<li className="flex items-center">
								<NavLink to="/error" className="flex justify-center items-center">
									error
								</NavLink>
							</li>

						</ul>
					</nav>

				</div>
			</div>
		</header>
	);
}

export default Header;
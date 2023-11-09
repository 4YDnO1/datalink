import  { NavLink } from "react-router-dom";
import logo from '../../../public/product_logo.svg'
import "./header.sass";
import logo1 from '../../../public/team_logo.svg'


function Header() {

	return (
		<header className="header-wrapper">
			<div className="content-container">
				<div className='content flex flex-wrap gap-2 py-4 w-full justify-between items-center'>

					<div className="flex justify-center flex-wrap gap-2">
						<a href="https://vitejs.dev" target="_blank" rel="noreferrer">
							<img className='w-[150px]' src={logo} alt="logo" />
						</a>
					</div>

					<nav className="flex items-center mx-10">
						<ul className="flex justify-center items-center flex-wrap gap-4">

							<li className="flex items-center">
								<NavLink to="/" className='flex justify-center items-center text-zinc-100 hover:text-zinc-300 transition-all hover:border-zinc-500'>
									Главная
								</NavLink>
							</li>
							<li className="flex items-center">
								<NavLink to="/error" className="flex justify-center items-center text-zinc-100 hover:text-zinc-300 transition-all">
									О нас
								</NavLink>
							</li>

						</ul>
					</nav>

					
					<div className='flex justify-center align-center flex-wrap gap-2 '>
						<a href="https://vitejs.dev" target="_blank" rel="noreferrer">
							<img className='w-[150px]' src={logo1} alt="logo" />
						</a>
					</div>

				</div>
			</div>
		</header>
	);
}

export default Header;
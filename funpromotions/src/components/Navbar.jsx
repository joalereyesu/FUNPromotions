import logo from './static/FUN_white.png'

const Navbar = () => {
    return (
        <header>
            <img src = {logo} className='logo' alt='logo'/> 
            <nav>
                <ul className='nav_links'>
                    <li><a key = 'concerts' href='/signup'>Concerts</a></li>
                    <li><a key='experience' href='/experience'>Experience</a></li>
                    <li><a key='profile' href='/profile'>Profile</a></li>
                    <li><a key='aboutUs' href='/about_us'>About us</a></li>
                </ul>
            </nav>
            <a className='btn' href='/'><button>Buy tickets</button></a>
        </header>
    );
};

export default Navbar;
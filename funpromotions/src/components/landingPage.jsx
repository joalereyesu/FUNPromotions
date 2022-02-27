import { Component } from "react";
import logo from './static/FUN_white.png';


class LandingPage extends Component {
    render() { 
        return (
            <div className="landing_cover">
                <div className="login_container">
                    <div className="logo_container">
                        <img className="login_logo" src={logo} alt="logo_login"/>
                    </div>
                    <div className="login_forms">
                        <h1>Log in</h1>
                    </div>
                </div>
            </div>
        );
    }
}
 
export default LandingPage;
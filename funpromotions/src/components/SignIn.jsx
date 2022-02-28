import { Component } from "react";
import logo from './static/FUN_white.png';


class SignIn extends Component {
    render() { 
        return (
            <div className="landing_cover">
                <div className="login_container">
                    <div className="logo_container">
                        <img className="login_logo" src={logo} alt="logo_login"/>
                    </div>
                    <div className="login_forms">
                        <h1>Log in</h1>
                        <form action="" method="POST" className="form" onSubmit={this.props.newUser}>
                            <div className="form-group">
                                <input type='text' className="form-control" name="username" placeholder="janeDoe34"></input>
                                <label for="username" className="form-label">Username</label>
                            </div>
                            <div className="form-group">
                                <input type='password' className="form-control" name="password" placeholder="janedoe12"></input>
                                <label for="password" className="form-label">Password</label>
                            </div>
                        </form>
                        <div className="center">
                            <button>Sign in</button>
                        </div>
                        <div className="p_container">
                        <p>If you do not have an account already, please <a href="/signup">sign up</a> and become a member of our family.</p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
 
export default SignIn;
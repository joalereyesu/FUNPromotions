import React, { useState } from 'react';
import logo from './static/FUN_white.png';
import firebase from "firebase/app"
import 'firebase/auth'

function SignUp (){
    const [data, setData] = useState({
        name: '',
        last_name: '', 
        username: '', 
        email: '', 
        password: ''
    });

    const handleSignUp = (event) => {
        setData({
            ...data, 
            [event.target.name] : event.target.value
        });
    }

    //const sendNewUser = (event) => {}
    

    return (
        <div className="landing_cover">
            <div className="login_container">
                <div className="logo_container">
                    <img className="signup_logo" src={logo} alt="logo_login"/>
                </div>
                <div className="signup_forms">
                    <h1>Create an account</h1>
                    <form action="" method="POST" className="form">
                        <div className="form-group">
                            <input type='text' className="form-control" name="name" placeholder="Jane" onChange={handleSignUp}></input>
                            <label for="name" className="form-label">Name</label>
                        </div>
                        <div className="form-group">
                            <input type='text' className="form-control" name="last_name" placeholder="Doe" onChange={handleSignUp}></input>
                            <label for="last-name" className="form-label">Last name</label>
                        </div>
                        <div className="form-group">
                            <input type='text' className="form-control" name="username" placeholder="janedoe132" onChange={handleSignUp}></input>
                            <label for="username" className="form-label">Username</label>
                        </div>
                        <div className="form-group">
                            <input type='text' className="form-control" name="email" placeholder="janedoe@example.com" onChange={handleSignUp}></input>
                            <label for="email" className="form-label">E-mail</label>
                        </div>
                        <div className="form-group">
                            <input type='password' className="form-control" name="password" placeholder="jd321" onChange={handleSignUp}></input>
                            <label for="pasword" className="form-label">Password</label>
                        </div>
                    </form>
                    <div className="center">
                        <button>Sign up</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

 
export default SignUp;
import React, { Component } from "react";
import axios from 'axios';
import './components/static/styles.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import SignIn from "./components/SignIn";
import SignUp from "./components/SignUp";
import Navbar from "./components/Navbar";
import HomePage from "./components/homePage";

class App extends Component {
  constructor(){
    super()
    this.state = {user: ''};

    this.handleNewUser = this.handleNewUser.bind(this);
  }


  handleNewUser = (newUser) => {
    this.setState({user: newUser.target.value})
    axios.post('/signup', this.state.user).then(response => {
      console.log(response)
    });
  };

  render() { 
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element = {<SignIn/>}></Route>
          <Route path="/signup" element = {<SignUp newUser={this.handleNewUser}/>}></Route>
        </Routes>
        <Navbar/>
        <Routes>
          <Route path="/:username" element = {<HomePage/>}></Route>
        </Routes>
      </BrowserRouter>

    );
  }
}
export default App;

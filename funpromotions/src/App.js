import { Component } from "react";
import './components/static/styles.css'

import Navbar from "./components/Navbar";
import LandingPage from "./components/landingPage";

class App extends Component {
  state = { 
    loggedIn : false
   } 

  render() { 
    return (
      <LandingPage/>
      //<Navbar/>
    );
  }
}
export default App;

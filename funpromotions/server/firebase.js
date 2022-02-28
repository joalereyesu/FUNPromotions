// Import the functions you need from the SDKs you need
import firebase from "firebase/app";
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBpRYnUqiBnlGcokgTCgqWtwfrItkD39hU",
  authDomain: "funpromotions-1e210.firebaseapp.com",
  projectId: "funpromotions-1e210",
  storageBucket: "funpromotions-1e210.appspot.com",
  messagingSenderId: "154565454708",
  appId: "1:154565454708:web:98410ba8f40f5cbac91a21",
  measurementId: "G-RBS1P35Z8H"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
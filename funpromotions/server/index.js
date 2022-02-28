const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
const { getFirestore, Timestamp, FieldValue } = require('firebase-admin/firestore');

  
initializeApp();

const db = getFirestore();

const express = require('express');
const { start } = require('repl');
const app = express();

let userNumber = 0;

app.get('/', (req, res)=> {

});

app.post('/signup', async(req, res)=> {
  userNumber ++;
  try {
    const {name, last_name, username, email, password} = req.body;
    console.log(name);
    const docRef = db.collection('FUNPusers').doc('user'+userNumber);
    docRef.set({
      name: name,
      last_name: last_name,
      username: username,
      email: email, 
      password: password
    });
    } catch (e) {
      console.error("Error adding document: ", e);
    }
}); 

app.get('/experience', (req, res)=> {

});
app.get('/about_us', (req, res)=> {

});

app.listen(3000, () => start());
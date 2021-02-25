// Firebase App (the core Firebase SDK) is always required and
// must be listed before other Firebase SDKs
import firebase from "firebase/app";

// Add the Firebase services that you want to use
import "firebase/auth";
import "firebase/database";

// TODO: Replace the following with your app's Firebase project configuration
// For Firebase JavaScript SDK v7.20.0 and later, `measurementId` is an optional field
var firebaseConfig = {
    apiKey: "AIzaSyDGzfvGakxeHjiKNSDNutURRW4QZlQnvyA",
    authDomain: "temporal-b129b.firebaseapp.com",
    databaseURL: "https://temporal-b129b.firebaseio.com",
    projectId: "temporal-b129b",
    storageBucket: "temporal-b129b.appspot.com",
    messagingSenderId: "505061257952",
    appId: "1:505061257952:web:8d7da1e66546d56a"
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

export default firebase;
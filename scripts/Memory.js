localStorage.setItem('testObject', JSON.stringify("hello world"));

// Retrieve the object from storage
var retrievedObject = localStorage.getItem('testObject');

console.log('retrievedObject: ', JSON.parse(retrievedObject));
$("#test").html(JSON.parse(retrievedObject))
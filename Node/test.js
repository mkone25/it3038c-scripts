var path = require("path");

var hello = "Hello from Node JS Variable!"
console.log('Printing variable hello: ${hello}');

console.log("directory name: "+ __dirname);
console.log("directory name and file name: "+ __filename)

console.log("Using path module:")
console.log('Hello from file ${path.basement(__filename)}');

console.log('Process args: ${process.argv}');

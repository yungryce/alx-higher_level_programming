#!/usr/bin/node
const data = require('./100-data.js').list;
// const mappedList = myList.map((value, index) => value * index);
// for (const index in myList) {
//   myList[index] *= index;
// }
const newList = [];
for (let i = 0; i < data.length; i++) {
  newList.push(i * data[i]);
}
console.log(data);
console.log(newList);

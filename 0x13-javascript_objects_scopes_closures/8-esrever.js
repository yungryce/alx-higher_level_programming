#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  // for (let i = list.length -1; i >= 0; i--) {
  // reversedList.push(i);
  // }
  for (const i in list) {
    reversedList.unshift(list[i]);
  }
  return reversedList;
};

#!/usr/bin/node
exports.addMeMaybe = function (x, myFunc) {
  myFunc(++x);
};

#!/usr/bin/node
const fs = require('fs');

// const fArg = fs.readFileSync(process.argv[2]).toString();
// const sArg = fs.readFileSync(process.argv[3]).toString();
const fArg = fs.readFileSync(process.argv[2], 'utf8');
const sArg = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], fArg + sArg);

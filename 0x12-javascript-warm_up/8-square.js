#!/usr/bin/node
const count = Number(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    console.log('X'.repeat(count));
  }
}

#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const num = Number(process.argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}

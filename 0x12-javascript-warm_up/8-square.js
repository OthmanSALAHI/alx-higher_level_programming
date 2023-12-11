#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
let i = 0;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
while (i < x) {
  let j = 0;
  let sq = '';
  while (j < x) {
    sq += 'X';
    j++;
  }
  console.log(sq);
  i++;
}

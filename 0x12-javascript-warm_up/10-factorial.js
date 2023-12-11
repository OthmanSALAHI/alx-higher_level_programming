#!/usr/bin/node
function fact (num) {
  if (num === 0) return 1;
  return num * fact(num - 1);
}
const number = parseInt(process.argv[2]);
const factor = isNaN(number) ? 1 : fact(number);
console.log(factor);

#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  const newArr = args.slice(2).map(Number).sort((a, b) => b - a);
  console.log(newArr[1]);
}

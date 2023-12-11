#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const args = process.argv;
const lwl = Math.floor(Number(args[2]));
const tani = Math.floor(Number(args[3]));
add(lwl, tani);

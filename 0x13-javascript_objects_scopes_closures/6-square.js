#!/usr/bin/node
const SquareF = require('./5-square');

class Square extends SquareF {
  charPrint (c) {
    if (!c) { c = 'X'; }
    let i = 0;
    while (i < this.height) {
      let j = 0;
      let strin = '';
      while (j < this.height) {
        strin += c;
        j++;
      }
      console.log(strin);
      i++;
    }
  }
}
module.exports = Square;

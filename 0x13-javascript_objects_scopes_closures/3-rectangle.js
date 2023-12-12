#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
    print() {
      let i = 0;
      while (i < this.height) {
        let j = 0;
        let strin = "";
        while (j < this.width) {
            strin += "X"
            j++;
        }
        console.log(strin);
        i++;
      }
    }
  }
  module.exports = Rectangle;
  
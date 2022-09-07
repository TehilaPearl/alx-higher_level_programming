#!/usr/bin/node
const Squarer = require('./5-square');
class Square extends Squarer {
  charPrint (c) {
    if (c !== undefined) {
      let row;
      let column;
      for (row = 1; row <= this.height; row++) {
        for (column = 1; column <= this.width; column++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;

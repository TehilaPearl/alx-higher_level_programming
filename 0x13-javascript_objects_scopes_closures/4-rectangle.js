#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) === true) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    let row;
    let column;
    for (row = 1; row <= this.height; row++) {
      for (column = 1; column <= this.width; column++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
    return (this.width, this.height);
  }

  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
    return (this.width, this.height);
  }
}
module.exports = Rectangle;

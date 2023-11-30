#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!this.checkForANumber(w) || !this.checkForANumber(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  checkForANumber (value) {
    if (value <= 0 || typeof value !== 'number') {
      return false;
    }
    return true;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;

#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 && h <= 0 && Number.isNaN(w) && Number.isNaN(h)) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
};

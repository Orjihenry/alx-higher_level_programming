#!/usr/bin/node

const args = process.argv[2];
const size = parseInt(args);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  }
}

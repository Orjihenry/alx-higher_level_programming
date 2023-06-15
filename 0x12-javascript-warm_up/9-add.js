#!/usr/bin/node

const factorial = (num) => {
  if (isNaN(num)) {
    return 1;
  }

  num = parseInt(num);

  if (num === 0) {
    return 1;
  }

  return num * factorial(num - 1);
};

const arg = process.argv[2];
console.log(factorial(arg));

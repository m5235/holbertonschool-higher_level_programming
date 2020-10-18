#!/usr/bin/node
// computes and prints a factorial
const n = process.argv[2];
function factorial (number) {
  if ((isNaN(number)) || (number === 1)) {
    return 1;
  } else {
    return parseInt(number) * factorial(parseInt(number) - 1);
  }
}

console.log(factorial(n));

#!/usr/bin/node

const MyArg = process.argv[2];
if (isNaN(MyArg, 10))  {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}

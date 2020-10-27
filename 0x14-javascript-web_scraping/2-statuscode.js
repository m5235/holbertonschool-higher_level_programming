#!/usr/bin/node
const fs = require('fs');
const f = process.argv[2];
const fun = process.argv[3];

fs.writeFile(f, fun, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
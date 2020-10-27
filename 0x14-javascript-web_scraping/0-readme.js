#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, txt) {
  if (error) {
    console.log(error);
  } else { process.stdout.write(txt.toString()); }
});

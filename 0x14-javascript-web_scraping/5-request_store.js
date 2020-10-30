#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const Url = process.argv[2];
const req = process.argv[3];
request.get(Url, (err, r, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(req, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

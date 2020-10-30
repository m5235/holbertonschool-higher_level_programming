#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const Url = process.argv[2];
const fPath = process.argv[3];
request(url, function (error, r, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fPath, body, 'utf-8');
  }
});

#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, r, body) => {
    if (error) { return console.log(error); }
    console.log('code: ' + r.statusCode);
  }
});

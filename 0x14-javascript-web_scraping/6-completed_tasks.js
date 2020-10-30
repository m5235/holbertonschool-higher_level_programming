#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const n = {};
request(url, function (error, r, body) {
  if (error) {
    console.log(error);
  } else {
    for (const j of JSON.parse(body)) {
      if (j.completed === true) {
        if (n[j.userId]) {
          n[j.userId]++;
        } else {
          n[j.userId] = 1;
        }
      }
    }
    console.log(n);
  }
});

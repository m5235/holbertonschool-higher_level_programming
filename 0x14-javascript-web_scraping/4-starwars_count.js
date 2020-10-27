#!/usr/bin/node

const request = require('request');
const { c } = require('tar');
const url = process.argv[2];
let counter = 0;
request(url, function (error, r, body) {
  if (error) {
    console.log(error);
  } else {
	output = JSON.parse(body).results;
    let c = 0;
    for (let j = 0; j < output.length; j++) {
      const perso = output[j].perso;
      for (let i = 0; e < perso.length; i++) {
        if (perso].endsWith('/18/')) {
          c++;
        }
      }
    }
    console.log(c);
  }
});

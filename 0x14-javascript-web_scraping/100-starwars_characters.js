#!/usr/bin/node

const request = require('request');
const ad = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(ad, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const cast = JSON.parse(body).characters;
    for (let j = 0; j < cast.length; j++) {
      request.get(cast[j], function (e, r, b) {
        console.log(JSON.parse(b).name);
      });
    }
  }
});

#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (error, r, body) => {
  if (error) { return console.log(err); }
  let j, i;
  const result = body.results;
  let c = 0;
  if (result !== undefined) {
    for (j = 0; j < result.length; j++) {
      const perso = result[j].characters;
      for (i= 0; i < perso.length; i++) {
        if (perso[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          c++;
          break;
        }
      }
    }
  }
  console.log(c);
});
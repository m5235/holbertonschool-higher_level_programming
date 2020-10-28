#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (error, r, body) => {
  if (error) { return console.log(error); }
  let j, i;
  const res = body.results;
  let c = 0;
  if (r !== undefined) {
    for (j = 0; j < res.length; j++) {
      const perso = res[j].characters;
      for (i = 0; i < perso.length; i++) {
        if (perso[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          c++;
          break;
        }
      }
    }
  }
  console.log(c);
});

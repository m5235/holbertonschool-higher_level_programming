#!/usr/bin/node

const request = require('request');
const Id = process.argv[2];
const Url = `https://swapi-api.hbtn.io/api/films/${Id}`;
request(Url, { json: true }, (error, r, body) => {
    if (error) { return console.log(error); }
    console.log(body.title);
  });

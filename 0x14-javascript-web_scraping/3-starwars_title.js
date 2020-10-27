#!/usr/bin/node

const request = require('request');
const Id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${_Id}`;
request(baseUrl, (error, response, body) => {
request(url, (error, r, body) => {
    if (error) { return console.log(error); }
    console.log(body.title);
});

#!/usr/bin/node

const Mylist = require('./100-data').Mylist;
console.log(Mylist);

console.log(Mylist.map((x, y) => x * y));

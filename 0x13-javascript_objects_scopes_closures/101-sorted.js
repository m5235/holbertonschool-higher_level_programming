#!/usr/bin/node

const dic = module.require('./101-data.js').dict;
const Newdic = {};

for (const k in dic) {
  if (Newdic[dic[k]] !== undefined) {
    Newdic[dic[k]].push(k);
  } else {
    Newdic[dic[k]] = [k];
  }
}
console.log(Newdic);

#!/usr/bin/node
const { file } = require('babel-types');
const f = require('compose-function');
const fs = require('fs');
const contentFile = process.argv[2];
const toWrite = process.argv[3];

fs.writeFile(f, w, 'utf-8', (error) => {
    if (error) throw error;
  }
});
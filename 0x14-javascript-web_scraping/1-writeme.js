#!/usr/bin/node
const fs = require('fs');
const f = process.argv[2];
const w = process.argv[3];

fs.writeFile(f, w, 'utf-8', (error) => {
    if (error) throw error;
  }
});

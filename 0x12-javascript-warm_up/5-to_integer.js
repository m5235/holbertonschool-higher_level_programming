#!/usr/bin/node

const Myarg = process.argv[2];
if (isNaN(Number(Myarg))){
	console.log('Not a number');
  } else {
	console.log('My number: ' + myArg);
  }
#!/usr/bin/node

exports.esrever = function (list) {
	const _list = [];
	for (let i = 0; i < list.length; i++) {
	  _list[i] = list[list.length - 1 - i];
	}
	return _list;
  };

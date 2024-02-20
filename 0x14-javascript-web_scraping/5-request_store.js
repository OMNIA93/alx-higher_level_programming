#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const encoding = 'utf8';
  fs.writeFile(process.argv[3], body, { encoding }, (err) => {
    if (err) {
      throw err;
    }
  });
});

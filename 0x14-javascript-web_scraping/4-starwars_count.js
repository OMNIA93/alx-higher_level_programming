#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  let x = 0;
  const dict = JSON.parse(body).results;
  const regex = /^(https?:\/\/)?(swapi-api\.alx-tools\.com|swapi\.co)\/api\/people\/18\/$/;
  Object.keys(dict).forEach(element => {
    dict[element].characters.forEach(character => {
      if (regex.test(character)) {
        x += 1;
      }
    });
  });
  console.log(x);
});

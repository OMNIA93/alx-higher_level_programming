#!/usr/bin/node
const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const dict = JSON.parse(body);
  dict.characters.forEach(character => {
    request.get(character, (err, res, body) => {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});

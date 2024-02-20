#!/usr/bin/node
const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const dict = JSON.parse(body);
  const characters = dict.characters;

  for (const characterUrl of characters) {
    try {
      const characterResponse = await new Promise((resolve, reject) => {
        request.get(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(body);
          }
        });
      });

      const character = JSON.parse(characterResponse);
      console.log(character.name);
    } catch (error) {
      console.error(error);
    }
  }
});

#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];

const fetchFilmDetails = (filmId) => {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

  request(apiUrl, (err, res, body) => {
    if (err) {
      console.error('Request failed:', err);
      return;
    }
    
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    if (!characterUrls || !Array.isArray(characterUrls)) {
      console.error('Error: No characters found in film data.');
      return;
    }

    characterUrls.forEach((url) => {
      request(url, (error, response, body) => {
        if (error) {
          console.error('Failed to fetch character:', error);
          return;
        }
        const characterInfo = JSON.parse(body);
        console.log(characterInfo.name);  // Print each character's name
      });
    });
  });
};

fetchFilmDetails(filmId);

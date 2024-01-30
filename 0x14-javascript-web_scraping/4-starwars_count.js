#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  const counter = body.split('/people/18/').length - 1;
  console.log(counter);
});

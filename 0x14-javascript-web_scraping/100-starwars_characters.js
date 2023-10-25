#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, res, body) {
    if (error) {
        console.log(error);
    }
    const dt = JSON.parse(body);
    const dT = dt.characters;
    for (const i of dT) {
        request.get(i, function (error, res, body_) {
            if (error) {
                console.log(error);
            }
            const dt_ = JSON.parse(body_);
            console.log(dt_.name);
        });
    }
});

/**
 * author kenneth.cruz@unah.hn
 * version 0.1.0
 * date 9/7/2021
 */

const fetchData = require('../utils/fetchData');
const API = "https://rickandmortyapi.com/api/character/";


//1. Count cuántos personajes hay en la API
//2. Llamado del primer elemento hacia el nombre del personaje
//3. Del personaje, traer su dimensión

fetchData(API)
    .then(data => {
        
        console.log(data.info.count);
        return fetchData(`${API}${data.results[0].id}`);
    })
    .then(data => {
        
        console.log(data.name);
        return fetchData(data.origin.url);
    })
    .then(data => {
        console.log(data.dimension);
    })
    .catch(error => {
        console.log(error);
    });
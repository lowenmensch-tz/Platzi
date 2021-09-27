/**
 * author kenneth.cruz@unah.hn
 * version 0.1.0
 * date 9/7/2021
 */

let XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
let API = "https://rickandmortyapi.com/api/character/";

function fetchData(url_api, callback) {
    
    let xhttp = new XMLHttpRequest();
    xhttp.open('GET', url_api, true);
    xhttp.onreadystatechange = function (event) {
        if (xhttp.readyState === 4) { //request finished and response is ready
            if (xhttp.status === 200) { //OK
                callback(null, JSON.parse(xhttp.responseText));
            } else {
                const error = new Error('Error ' + url_api);
                return callback(error, null);
            }
        }
    }
    xhttp.send();
}


fetchData(API, function (error1, data1) {

    if (error1) return console.error(error1);
    
    fetchData(API + data1.results[0].id, function (error2, data2) {

        if (error2) return console.error(error2);
        
        //Traer origen de mi personaje
        fetchData(data2.origin.url, function (error3, data3) {

            if (error3) return console.error(error3);
            //Cantidad de personajes
            console.log(data1.info.count);
            //Nombre de mi personaje
            console.log(data2.name);
            //Nombre de mi origen
            console.log(data3.dimension);

        })
    })
})
/**
 * author kenneth.cruz@unah.hn
 * version 0.1.0
 * date 9/7/2021
 */


let XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

const fetchData=(url_api) => {

    return new Promise((resolve, reject)=>{

            const xhttp = new XMLHttpRequest();
            xhttp.open('GET', url_api, true);
            xhttp.onreadystatechange = (() => {

                if (xhttp.readyState === 4) { //request finished and response is ready

                    //request finished and response is ready
                    (xhttp.status === 200)
                    ? resolve(JSON.parse(xhttp.responseText))
                    : reject(new Error(`Error `, url_api));    

                }
            });

            xhttp.send();

        });
}


module.exports=fetchData;
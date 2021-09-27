/**
 * author kenneth.cruz@unah.hn
 * version 0.1.0
 * date 9/7/2021
 */


const somethingWillHappen = () => {

    return new Promise((resolve, reject) => {

        if(true){
            resolve('Hey!');
        }else{
            reject('Ups!');
        }
    });
};


somethingWillHappen()
    .then(response => console.log(response))
    .catch(error => console.log(error));


const somethingWillHappen2 = () => {

    return new Promise((resolve, reject) => {

        if(true){
            setTimeout(() => {
                resolve('Hey!');
            }, 2000);
        }else{
            const error = new Error('Ups!');
            reject(error);
        }
    });
}

somethingWillHappen2()
    .then(response => console.log(response))
    .catch(error => console.log(error));


//Ejecutar promesas encadenadas    
Promise.all([somethingWillHappen(), somethingWillHappen2()])
    .then(response => console.log(`Array of results: ${response}`))
    .catch(error => console.log(error));
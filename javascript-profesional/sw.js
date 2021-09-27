
/***
 * @author kenneth.cruz@unah.hn
 * @date 9/6/2021
 * @version 0.0.1
 */

const version = "v1";

self.addEventListener('install', event => {
    event.waitUntil(precache());
});


self.addEventListener('fetch', event => {
    const request = event.request;

    //get
    if(request.method != "GET"){
        return;
    }


    //BUSCAR EN CACHE
    event.respondWith(cacheResponse(request));

    //ACTUALIZAR CACHE
    event.waitUntil(updateCache(request));
});     


async function precache(){
    const cache = await caches.open(version);
    
    return cache.addAll([
        // '/',
        // '/index.html',
        // '/assets/index.js',
        // '/assets/MediaPlayer.js',
        // '/assets/plugins/AutoPlay.js',
        // '/assets/plugins/AutoPause.js',
        // '/assets/index.css',
        // '/assets/BigBuckBunny.mp4',
    ]);
}



async function cacheResponse(request){

    const cache = await caches.open(version);
    const response = await cache.match(request);

    return response || fetch(request);
}


async function updateCache(request){

    const cache = await caches.open(version);
    const response = await fetch(request);

    cache.put(request, response);
}
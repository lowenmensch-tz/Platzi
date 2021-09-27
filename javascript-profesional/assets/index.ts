/***
 * @author kenneth.cruz@unah.hn
 * @date 9/1/2021
 * @version 0.0.1
 */

import MediaPlayer from "./MediaPlayer";
import AutoPlay from "../plugins/AutoPlay";
import AutoPause from "../plugins/AutoPause";

const video = document.querySelector("video");
const playButton: HTMLElement = document.getElementById("playButton");
const muteButton: HTMLElement = document.getElementById("muteButton");

const player = new MediaPlayer(
        { 
            el: video,
            plugins: [new AutoPlay(), new AutoPause()],
        }
    );

playButton.onclick = () => player.togglePlay();      

muteButton.onclick = () => {

    if(player.media.muted){
        player.unmute();
    }else{
        player.mute();
    }
};


if("serviceWorker" in navigator){
 
     navigator.serviceWorker.register("/sw.js").catch(error => {
        console.log(error.message);
    });
}
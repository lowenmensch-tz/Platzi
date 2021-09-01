/***
 * @author kenneth.cruz@unah.hn
 * @date 9/1/2021
 * @version 0.0.1
 */

import MediaPlayer from "./MediaPlayer.js";
import AutoPlay from "/plugins/AutoPlay.js";

const video = document.querySelector("video");
const playButton = document.querySelector("button");

const player = new MediaPlayer(
        { 
            el: video,
            plugins: [new AutoPlay()],
        }
    );
playButton.onclick = () => player.togglePlay();      
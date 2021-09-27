/***
 * @author kenneth.cruz@unah.hn
 * @date 9/1/2021
 * @version 0.0.1
 */

import MediaPlayer from "../assets/MediaPlayer";

class AutoPlay {
    constructor() { }
    run(player: MediaPlayer) {


        if (!player.media.muted) {

            player.media.muted = true;
        }
        player.play();
    }
}



export default AutoPlay;
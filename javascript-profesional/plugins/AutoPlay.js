/***
 * @author kenneth.cruz@unah.hn
 * @date 9/1/2021
 * @version 0.0.1
 */

function AutoPlay(){}


AutoPlay.prototype.run = function(player){

    player.mute();
    player.play();
};

export default AutoPlay;
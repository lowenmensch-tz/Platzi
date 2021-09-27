/***
 * @author kenneth.cruz@unah.hn
 * @date 9/1/2021
 * @version 0.0.1
 */


class MediaPlayer {
    media: HTMLMediaElement;
    plugins: Array<any>;

    constructor(config) {
        this.media = config.el;
        this.plugins = config.plugins || [];

        this.initPlugins();
    }
    
    private initPlugins() {

        this.plugins.forEach(plugin => {
            plugin.run(this);
        });

    }
    play() {

        this.media.play();

    }
    pause() {

        this.media.pause();

    }
    mute() {

        this.media.muted = true;

    }
    unmute() {

        this.media.muted = false;

    }
    togglePlay() {

        (this.media.paused) ? this.play() : this.pause();

    }
    toggleMute() {

        (this.media.muted) ? this.unmute() : this.mute();

    }
}

export default MediaPlayer;
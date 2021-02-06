$(function() {
  console.log('Loaded Main');

  const screenHandler = new ScreenHandler();

  function setVideoStream(data) {
    const video = data.el;
    video.srcObject = data.stream;
  }

  function onLocalStream(stream) {
    console.log('onLocalStream', stream);

    setVideoStream({
      el: document.querySelector('#local-video'),
      stream: stream,
    });
  }

  function startScreenShare() {
    screenHandler.start((stream) => {
      onLocalStream(stream);
    });
  }

  function bindEvent() {
    document.querySelector('#btn-start').onclick = startScreenShare;
  }

  function initialize() {
    bindEvent();
  }

  initialize();
});


function ScreenHandler() {
  console.log('Loaded ScreenHandler', arguments);

  // REF https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints#Properties_of_shared_screen_tracks
  const constraints = {
    video: {
      width: 1980, // 최대 너비
      height: 1080, // 최대 높이
      frameRate: 10, // 최대 프레임
    },
  };
  let localStream = null;

  function getCrossBrowserScreenCapture() {
    if (navigator.getDisplayMedia) {
      return navigator.getDisplayMedia(constraints);
    } else if (navigator.mediaDevices.getDisplayMedia) {
      return navigator.mediaDevices.getDisplayMedia(constraints);
    }
  }

  function start(callback) {
    getCrossBrowserScreenCapture().then(
      (stream) => {
        console.log('Success getDisplayMedia', stream);
        localStream = stream;
        callback(localStream);
      },
      (error) => {
        console.error('Error getDisplayMedia', error);
      }
    );
  }

  function end(callback) {
    localStream.getTracks().forEach((track) => {
      track.stop();
    });

    callback && callback();
  }

  this.start = start;
  this.end = end;
}
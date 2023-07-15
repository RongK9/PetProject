const videoElement = document.getElementById("video");
const button = document.getElementById("button");
const button2 = document.getElementById("button2");
let isInPIPMode = false;

// Toggle PIP mode
function togglePIPMode() {
  if (isInPIPMode) {
    // Exit PIP mode
    if (document.pictureInPictureElement) {
      document.exitPictureInPicture();
    }
    button2.textContent = "Enter PIP mode";
    isInPIPMode = false;
  } else {
    // Enter PIP mode
    if (videoElement !== document.pictureInPictureElement) {
      videoElement.requestPictureInPicture();
    }
    button2.textContent = "Exit PIP mode";
    isInPIPMode = true;
  }
}

//Prompt to select media stream, pass to video element, then play
async function selectMediaStream() {
  try {
    const mediaStream = await navigator.mediaDevices.getDisplayMedia();
    videoElement.srcObject = mediaStream;
    videoElement.onloadedmetadata = () => {
      videoElement.play();
    };
  } catch (error) {
    // Catch error here
    console.log("Whoops, error here:", error);
  }
}
button.addEventListener("click", selectMediaStream);
// Attach click event listener to the Enter/Exit PIP mode button
button2.addEventListener("click", togglePIPMode);


function togglePIPMode ()
document.addEventListener("DOMContentLoaded", function () {
    const videoFeed = document.getElementById("videoFeed");
    const toggleButton = document.getElementById("toggleButton");

    let isStreaming = true;

    toggleButton.addEventListener("click", function () {
        if (isStreaming) {
            videoFeed.src = "";  // หยุดการแสดงผล
            toggleButton.textContent = "Start";
        } else {
            videoFeed.src = "/video_feed";  // เริ่มการแสดงผลใหม่
            toggleButton.textContent = "Stop";
        }
        isStreaming = !isStreaming;
    });
});

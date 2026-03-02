// Background Music
const audio = new Audio('assets/audio/bgm.mp3');
audio.loop = true;
audio.volume = 0.5;

// Track audio state
let audioEnabled = false;

// Function to start audio
function startAudio() {
    if (!audioEnabled) {
        audio.play().then(() => {
            audioEnabled = true;
            console.log('🎵 Audio started!');
            // Hide instruction if exists
            const instruction = document.getElementById('audio-instruction');
            if (instruction) {
                instruction.style.opacity = '0';
                instruction.style.pointerEvents = 'none';
            }
        }).catch(err => {
            console.log('Audio play failed:', err);
        });
    }
}

// Try to play on page load
document.addEventListener('DOMContentLoaded', () => {
    startAudio();
});

// Allow audio to start on any user interaction
document.addEventListener('click', startAudio);
document.addEventListener('touchstart', startAudio);

// Synchronized Lyrics
const lyrics = [
    { time: 0, text: "Ho teri malmal ki kurti gulabi ho gayi… Manchali chaal kaise nawaabi ho gayi…" },
    { time: 5, text: "Balam pichkari jo tune mujhe maari… Toh seedhi saadhi chhori sharaabi ho gayi…" },
    { time: 7, text: "Haan jeans pehen ke jo tune maara thumka… Toh lattoo padosan ki bhabhi ho gayi…" },
];

const lyricsBox = document.getElementById('lyrics-box');

function syncLyrics() {
    const currentTime = audio.currentTime;
    const currentLyric = lyrics.find(lyric => currentTime >= lyric.time && currentTime < (lyric.time + 10));
    if (currentLyric) {
        lyricsBox.textContent = currentLyric.text;
    }
}

setInterval(syncLyrics, 500);

// Color Shower Animation
const effectButton = document.getElementById('effect-button');
const holiColors = [
    '#FF1493', // Deep Pink
    '#FFD700', // Gold
    '#00CED1', // Dark Turquoise
    '#FF69B4', // Hot Pink
    '#32CD32', // Lime Green
    '#FF4500', // Orange Red
    '#9370DB', // Medium Purple
    '#FF6347', // Tomato
    '#00FA9A', // Medium Spring Green
    '#FFB6C1'  // Light Pink
];

effectButton.addEventListener('click', () => {
    createColorShower();
});

function createColorShower() {
    for (let i = 0; i < 150; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.backgroundColor = holiColors[Math.floor(Math.random() * holiColors.length)];
        particle.style.left = Math.random() * 100 + 'vw';
        particle.style.animationDuration = (Math.random() * 2 + 3) + 's';
        particle.style.width = (Math.random() * 8 + 5) + 'px';
        particle.style.height = particle.style.width;
        
        document.body.appendChild(particle);
        
        setTimeout(() => {
            particle.remove();
        }, 5000);
    }
}
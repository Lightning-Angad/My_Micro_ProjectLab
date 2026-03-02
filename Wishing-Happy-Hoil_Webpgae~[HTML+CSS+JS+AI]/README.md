# 🎨 Colorful Holi Celebration Responsive Webpage

A vibrant, interactive, and fully responsive Holi celebration webpage built with HTML, CSS, and JavaScript.

## 📁 Project Structure

```
holi-webpage/
├── index.html                    # Main HTML file
├── css/
│   ├── style.css               # Main stylesheet with animations
│   └── responsive.css          # Responsive design for all devices
├── js/
│   └── main.js                 # JavaScript for interactivity
├── assets/
│   ├── images/
│   │   └── bg.jpg             # Background image (add your image here)
│   └── audio/
│       └── bgm.mp3            # Background music (add your audio here)
└── README.md                   # This file
```

## ✨ Features

### 1. **Gradient Heading**
- "HAPPY HOLI" text with animated 5-color gradient (Red, Orange, Yellow, Green, Blue)
- Responsive font sizing for all devices

### 2. **Synchronized Lyrics Glass Box**
- Translucent glass effect with blur
- Time-synced lyrics display (Spotify-style)
- Lyrics change automatically with audio playback

### 3. **Interactive Button**
- "CLICK FOR EFFECT" button with hover/active animations
- Triggers vibrant color shower animation on click

### 4. **Color Shower Animation**
- 150+ colorful particles falling from top
- 10 different Holi colors
- Smooth animation with fade-out effect

### 5. **Responsive Design**
- **Mobile**: Optimized for screens up to 600px
- **Tablet**: Optimized for screens 601px to 1024px
- **Desktop**: Full experience for 1025px and above

### 6. **Footer**
- Gradient text credits
- Dark semi-transparent background
- Creator attribution

## 🎵 Audio Setup

1. Add your Holi song to `assets/audio/bgm.mp3`
2. The audio will:
   - Auto-play (with browser permission)
   - Loop continuously
   - Sync with lyrics display
   - Allow user interaction fallback

### Supported Audio Formats
- MP3
- WAV
- OGG
- M4A

## 🖼️ Image Setup

1. Add a colorful Holi background image to `assets/images/bg.jpg`
2. Recommended specifications:
   - Size: 1920x1080px or higher
   - Format: JPG/PNG
   - The image will be automatically covered with a dark gradient overlay

### Example Image Ideas
- Holi celebration with throwing colors
- Colorful powder clouds
- Festival fireworks
- Colorful bokeh background

## 🎨 Color Palette

The animation uses these vibrant Holi colors:
- Deep Pink (#FF1493)
- Gold (#FFD700)
- Dark Turquoise (#00CED1)
- Hot Pink (#FF69B4)
- Lime Green (#32CD32)
- Orange Red (#FF4500)
- Medium Purple (#9370DB)
- Tomato (#FF6347)
- Medium Spring Green (#00FA9A)
- Light Pink (#FFB6C1)

## 🚀 How to Use

1. **Open the webpage**: Simply open `index.html` in any modern web browser
2. **Enable audio**: Click anywhere on the page to enable auto-play audio
3. **Trigger effects**: Click the "CLICK FOR EFFECT" button to see the color shower animation
4. **Responsive view**: Resize your browser or open on mobile/tablet to see responsive design

## 🌐 Browser Compatibility

✅ Chrome/Edge (recommended)
✅ Firefox
✅ Safari
✅ Opera
⚠️ Internet Explorer 11 (limited support)

## 📝 Customization

### Change Colors
Edit the `holiColors` array in `js/main.js` to customize particle colors

### Adjust Animation Speed
- Change `animationDuration` in the particle creation (main.js)
- Modify `@keyframes fall` timing in `css/style.css`

### Modify Text
- Update greeting text in `index.html`
- Change lyrics in `js/main.js` (update time and text)
- Modify footer text as needed

### Adjust Particle Count
- Change the loop count (currently 150) in `createColorShower()` function in `main.js`

## 📱 Features by Device

### Desktop
- Full-size greeting (4rem)
- 80% width lyrics box
- Large button with shadow effects
- 150 particles on click

### Tablet
- Medium greeting (3.5rem)
- 85% width lyrics box
- Responsive button sizing

### Mobile
- Compact greeting (2.5rem)
- 90% width lyrics box (better readability)
- Optimized button size

## ⚠️ Known Limitations

1. **Audio Auto-play**: Some browsers block auto-play. Click the page to enable.
2. **Background Image**: Add your own image to `assets/images/bg.jpg`
3. **First Load**: Assets may need to be properly linked if moved

## 🎯 Requirements Checklist

- ✅ Exact visual match with reference design
- ✅ Fully responsive (PC, Tablet, Mobile)
- ✅ Automatic looping background music
- ✅ Spotify-style synchronized lyrics
- ✅ Interactive color shower animation
- ✅ Proper folder organization
- ✅ No broken files
- ✅ Smooth performance

## 📄 License & Credits

Made with Love by Lightning-Angad 🌟
Designed with Figma & Vibe-Coded with Copilot & ChatGPT

## 🤝 Support

For issues or questions:
1. Ensure all files are in the correct folder structure
2. Check browser console for error messages (F12)
3. Verify audio and image files are in the assets folder
4. Try a different browser if experiencing issues

---

**Enjoy your colorful Holi celebration! 🎨🎉**

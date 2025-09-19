const fontName = "Roboto";
const fontURL = `https://fonts.googleapis.com/css2?family=${fontName.replace(/ /g, '+')}&display=swap`;

document.getElementById("changeFont").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.insertCSS({
      target: { tabId: tabs[0].id },
      css: `
        @import url('${fontURL}');
        * {
          font-family: '${fontName}', sans-serif !important;
        }
      `
    });
  });
});

document.getElementById("revertFont").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.insertCSS({
      target: { tabId: tabs[0].id },
      css: `
        * {
          font-family: initial !important;
        }
      `
    });
  });
});
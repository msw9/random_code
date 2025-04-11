browser.contextMenus.create({
  id: "noNewLine",
  title: "No New Line",
  contexts: ["selection"]
});

browser.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "noNewLine") {
    browser.tabs.sendMessage(tab.id, { action: "noNewLine" });
  }
});
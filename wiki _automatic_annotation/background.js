browser.contextMenus.create({
  id: "addBraces",
  title: "Add Braces",
  contexts: ["selection"]
});

browser.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "addBraces") {
    browser.tabs.sendMessage(tab.id, { action: "addBraces" });
  }
});
browser.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "addBraces") {
 const myTextarea = document.getElementById("wpTextbox1"); 
	myTextarea.focus();
    const start = myTextarea.selectionStart;
    const end = myTextarea.selectionEnd;
    const selectedText = myTextarea.value.substring(start, end);
	const newText = `{{a|${selectedText}|0|2}}`;
	myTextarea.value = myTextarea.value.substring(0, start) + newText + myTextarea.value.substring(end);
    myTextarea.selectionStart = start; 
    myTextarea.selectionEnd = start + newText.length; 
    sendResponse({ success: true });
  }
});

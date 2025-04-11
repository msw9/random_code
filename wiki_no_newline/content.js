browser.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "noNewLine") {
 const myTextarea = document.getElementById("wpTextbox1"); 
	myTextarea.focus();
    const start = myTextarea.selectionStart;
    const end = myTextarea.selectionEnd;
    const selectedText = myTextarea.value.substring(start, end);
	const newText = selectedText.replace(/\n/g," ").toString();
	console.log(newText);
	myTextarea.value = newText;
    myTextarea.selectionStart = start; 
    myTextarea.selectionEnd = start + newText.length; 
    sendResponse({ success: true });
  }
});
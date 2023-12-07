function checkCopy() {
    const inputText = $('#inputText').val();
    
    // You can implement your copy-checking logic here
    // For simplicity, let's just check if the text contains "copy"
    const result = inputText.toLowerCase().includes('copy');

    if (result) {
        $('#result').text('This text contains potential copy.');
    } else {
        $('#result').text('No copy detected.');
    }
}

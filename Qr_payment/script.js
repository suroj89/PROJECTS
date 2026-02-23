function generateQR() {
    const upiId = document.getElementById('upiId').value.trim();
    const amount = document.getElementById('amount').value.trim();
    
    if (!upiId || !amount) {
        alert("Please enter UPI ID and Amount!");
        return;
    }

    const upiLink = `upi://pay?pa=${upiId}&pn=Receiver&am=${amount}&cu=INR`;
    
    const qrDiv = document.getElementById('qrcode');
    qrDiv.style.display = 'flex';
    qrDiv.innerHTML = '';
    
    new QRCode(qrDiv, {
        text: upiLink,
        width: 180,
        height: 180
    });

    document.getElementById('result').classList.remove('hidden');
}

function payNow() {
    const upiId = document.getElementById('upiId').value.trim();
    const amount = document.getElementById('amount').value.trim();
    window.location.href = `upi://pay?pa=${upiId}&pn=Receiver&am=${amount}&cu=INR`;
}
document.getElementById('prescription-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const drug = document.getElementById('drug').value;
    const quantity = document.getElementById('quantity').value;

    fetch('/prescribe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ drug: drug, quantity: quantity }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

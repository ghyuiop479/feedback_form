document.getElementById('feedbackForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const data = {
        name: document.getElementById('name').value,
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value,
        message: document.getElementById('message').value
    };

    fetch('/send_feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => alert('Feedback sent!'))
    .catch(err => alert('Error sending feedback'));
});

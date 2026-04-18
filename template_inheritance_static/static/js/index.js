// document.getElementById('user-form').addEventListener('submit', function(event) {
//     event.preventDefault(); // Prevent the default form submission 

//     let userData = {
//         name: document.getElementById('name').value,
//         age: document.getElementById('age').value,
//         hobbies: document.getElementById('hobbies').value
//     }

//     console.log('User Data:', userData);
//     fetch('submit/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(userData)
//     })
//     .then(async response => {
//         const contentType = response.headers.get('content-type');
//         if (contentType && contentType.indexOf('application/json') !== -1) {
//             const data = await response.json();
//             console.log('Success:', data);
//         } else {
//             const text = await response.text();
//             console.error('Error: Response is not JSON:', text);
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });
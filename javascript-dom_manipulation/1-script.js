const button = document.querySelector('#red_header');
const header = document.querySelector('header');

button.addEventListener('click', () => {
    header.style.color = 'red';
});
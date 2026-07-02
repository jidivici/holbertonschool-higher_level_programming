const button = document.querySelector('#red_header');
const header = document.querySelector('header');

button.addEventListener('click', () => {
    header.classList.add('red');
});
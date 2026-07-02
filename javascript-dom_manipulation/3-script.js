const header = document.querySelector('header');

document.querySelector('#toggle_header').addEventListener('click', () => {
    header.classList.toggle('red');
    header.classList.toggle('green');
});
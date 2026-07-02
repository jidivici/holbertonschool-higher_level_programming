const list = document.querySelector('.my_list');

document.querySelector('#add_item').addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.appendChild(li);
});
const updateUserInfo = response => {
    console.log(response);
    let data = response.data.results[0];

    let name = document.querySelector('#name');
    let username = document.querySelector('#username')
    let email = document.querySelector('#email');
    let phone = document.querySelector('#phone');
    let street = document.querySelector('#street');
    let city = document.querySelector('#city');
    let state = document.querySelector('#state');
    let zip = document.querySelector('#zip');

    name.innerText += `${data.name.title} ${data.name.first} ${data.name.last}`;
    username.innerText += `${data.login.username}`;
    email.innerText += `${data.email}`;
    phone.innerText += `${data.cell}`;
    street.innerText += `${data.location.street.number} ${data.location.street.name}`;
    city.innerText += `${data.location.city}`;
    state.innerText += `${data.location.state}`;
    zip.innerText += `${data.location.postcode}`;
}

const callAPI = () => {
    let url = "https://randomuser.me/api/?format=JSON";
    
    axios.get(url)
        .then(response => {
            updateUserInfo(response);
        });
}

const moveCookies = targ => {
    let cookieJar = document.querySelector('#cookie-jar');
    targ.innerHTML = cookieJar.innerHTML;
    cookieJar.innerHTML = "Ooooh, mom's gonna be maaaad!";
}

const randomColorAndSize = targ => {
    let r = Math.random() * 255;
    let g = Math.random() * 255;
    let b = Math.random() * 255;

    targ.style.color = `rgb(${r},${g},${b})`;
    targ.style.fontSize = `${Math.random() * 3 + .5}rem`;
    targ.style.textShadow = `0 0 10px rgb(${r},${g},${b})`;
    
}

const gimmeBtn = document.querySelector('.gimme-btn');

gimmeBtn.addEventListener('click', (event) => {
    let target = document.querySelector('#cookies');
    moveCookies(target);
});

const container = document.querySelector('.container');
const firstLine = document.querySelector(".item1");
let newFirstLine = document.createElement('div');
newFirstLine.classList.add('item1');

for(let i=0; i<firstLine.innerText.length; i++){
    let char = document.createElement('span');
    char.innerText = firstLine.innerText[i];
    randomColorAndSize(char);
    newFirstLine.append(char);
}
firstLine.remove();
container.prepend(newFirstLine);

callAPI();
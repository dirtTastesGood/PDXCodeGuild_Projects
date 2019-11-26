window.addEventListener('load', () => {
    let counter = 5;
    const timer = setInterval(() => {
                document.querySelector('.count').innerText = counter;
                counter--;

                if(counter < 0){
                    const urls = ['https://pbfcomics.com/', 'https://sarahcandersen.com/', 'https://www.boltcityproductions.com/', 'http://www.rice-boy.com/', 'https://abstrusegoose.com/'];
                    let choice = Math.floor(Math.random() * urls.length);
                    window.location = urls[choice];
                }
        }, 1000);
});

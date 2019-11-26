window.addEventListener('load', () => {
    const urls = ['https://pbfcomics.com/', 'https://sarahcandersen.com/', 'https://www.boltcityproductions.com/', 'http://www.rice-boy.com/', 'https://abstrusegoose.com/'];
    let choice = Math.floor(Math.random() * urls.length);
    window.location = urls[choice];
});

const callApi = () => {
    axios.get('https://favqs.com/api/quotes/?page=2&filter=love', {
        headers: {
            'Authorization': `Token token="${favqs_api_key}"`
        }
    })
    .then(response => {
        displayQuotes(response.data);
        console.log(response.data);
    });
}

// const sortQuotes = (quotes, filter) => {

// }

const displayQuotes = response => {
    const qBody = document.querySelector('#quote-text');
    const qAuthor = document.querySelector('#quote-author');

    let quote = response.quotes[ Math.floor(Math.random() * response.quotes.length)]

    qBody.innerText = quote.body;
    qAuthor.innerText = quote.author;
}

callApi();
const callApi = () => {
    axios.get('https://favqs.com/api/quotes', {
        headers: {
            'Authorization': `Token token="${favqs_api_key}"`
        }
    })
    .then(response => {
        displayQuote(response.data);
        console.log(response.data);
        
    });
}

const displayQuote = response => {
    const qBody = document.querySelector('#quote-body');
    const qAuthor = document.querySelector('#quote-author');    

    let quote = response.quotes[ Math.floor(Math.random() * response.quotes.length)]

    qBody.innerText = quote.body;
    qAuthor.innerText = quote.author;
}

callApi();
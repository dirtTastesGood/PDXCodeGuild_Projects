const callApi = (page=1, filter) => {

    filter = filter.replace("\"", "");

    let url = `https://favqs.com/api/quotes/?page=${page}&filter=${filter}`;

    axios.get(url, {
        headers: {
            'Authorization': `Token token="${favqs_api_key}"`
        }
    })
    .then(response => {
        displayQuotes(response.data);
        console.log(response.data);
    });
}

const buildQuoteCard = index => {
    const quotesList = document.querySelector('#quotes-list');

    let newQuote = document.createElement('div');
    newQuote.classList.add('quote-card');
    newQuote.id = `quote-card-${index}`;
    
    let lilQBody = document.createElement('div');
    lilQBody.classList.add('quote-body');
    lilQBody.id = `quote-body-${index}`;
    newQuote.append(lilQBody);

    let lilQAuthor = document.createElement('div');
    lilQAuthor.classList.add('quote-author');
    lilQAuthor.id = `quote-author-${index}`
    newQuote.append(lilQAuthor);

    quotesList.append(newQuote);
}

const displayQuotes = response => {
    const quotesList = document.querySelector('#quotes-list');

    const bigQBody = document.querySelector('#quote-text');
    const bigQAuthor = document.querySelector('#quote-author');

    let quote = response.quotes[ Math.floor(Math.random() * response.quotes.length)]

    bigQBody.innerText = quote.body;
    bigQAuthor.innerText = quote.author;

    for(let i=0; i<response.quotes.length; i++){
        buildQuoteCard(i);

        let qBody = document.querySelector(`#quote-body-${i}`);
        let qAuthor = document.querySelector(`#quote-author-${i}`);

        qBody.innerText = response.quotes[i].body;
        qAuthor.innerText = response.quotes[i].author;
    }

}

callApi(2,"inspiration");
const callApi = (filter, filterType="", page=1) => {
    filter = filter.replace("\"", "");

    let url;

    if(filterType == ""){
        url = `https://favqs.com/api/quotes/?page=${page}&filter=${filter}`;
    } else {
        filterType = filterType.replace("\"", "");
        console.log(`type: ${filterType}`);
        
        
        url = `https://favqs.com/api/quotes/?filter=${filter}&type=${filterType}&page=${page}`;
        console.log(`url: ${url}`);
    }

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

    let lilQTagList = document.createElement('div');
    lilQTagList.classList.add('tag-list');
    lilQTagList.id = `tag-list-${index}`;
    newQuote.append(lilQTagList);

    quotesList.append(newQuote);
}

const displayAuthors = response => {

}

const displayQuotes = response => {
    const quotesList = document.querySelector('#quotes-list');

    const bigQBody = document.querySelector('#quote-text');
    const bigQAuthor = document.querySelector('#quote-author');

    let quote = response.quotes[ Math.floor(Math.random() * response.quotes.length)]

    bigQBody.innerHTML = quote.body;
    bigQAuthor.innerHTML = quote.author;

    for(let i=0; i<response.quotes.length; i++){
        buildQuoteCard(i);

        let qBody = document.querySelector(`#quote-body-${i}`);
        let qAuthor = document.querySelector(`#quote-author-${i}`);
        let qTags = document.querySelector(`#tag-list-${i}`);

        qBody.innerHTML = response.quotes[i].body;
        qAuthor.innerHTML = response.quotes[i].author;

        for(let j=0; j<response.quotes[i].tags.length; j++){
            let tag = document.createElement('div');
            tag.classList.add('tag');
            tag.innerHTML = response.quotes[i].tags[j];
            qTags.append(tag);
        }
        
    }
}

const submitForm = () => {
    let filter = document.querySelector('#filter-input').value;
    let filterType = document.querySelector('#search-by').value
    
    callApi(filter, filterType, page=1); // page variable hardcoded until pagination added
}

const submitBtn = document.querySelector('#submit');
submitBtn.addEventListener('click', () => {
    console.log("CALLED");

    submitForm();
    
});
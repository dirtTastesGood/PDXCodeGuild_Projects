function giveAdvice(score){
    let msg;
    if(score < 17){
        msg = "You should hit.";
    } if(score >= 17 && score < 21){
        msg = "You should stay."
    } if(score == 21) {
        msg = "Blackjack";
    } if(score > 21) {
        msg = "You busted."
    }

    return msg
}

function getScore(cards){

    const scores = {"a":11,
                    "2":2,
                    "3":3,
                    "4":4,
                    "5":5,
                    "6":6,
                    "7":7,
                    "8":8,
                    "9":9,
                    "10":10,
                    "j": 10,
                    "q": 10,
                    "k": 10
    }
    
    let handScore = 0;

    for(let i=0; i<cards.length; i++){

        handScore += scores[cards[i]];
    }

    return handScore
}

function main(){
    const readline = require('readline-sync');

    let cards = [];
    while(cards.length < 3 ){
        let card = readline.question('Enter your card: (enter \'q\' to quit): ');

        if(card.toLowerCase() === 'q'){
            break
        } else {
            cards.push(card);
        }
    }    

    let score = getScore(cards);
    let msg = giveAdvice(score);

    console.log(msg);
    
    
}

main();
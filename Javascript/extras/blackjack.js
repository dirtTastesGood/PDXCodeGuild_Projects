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
                    // "A": 11
    }
    
    let handScore = 0;

    for(let i=0; i<cards.length; i++){
        // if(cards[i].toLowerCase() == 'a'){
        //     if(handScore + scores['A'] > 21){
        //         cards[i] = 'a';
        //     } else {
        //         cards[i] = 'A';
        //     }
        // }
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

    console.log(getScore(cards));
    
}

main();
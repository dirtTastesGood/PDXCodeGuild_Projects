function pick6(){
    let ticket = [];

    for(let i=0; i<6; i++){
        ticket.push(Math.ceil(Math.random()*99));
    }

    return ticket
}

function countMatches(ticket, winningTicket){
    let match_count = 0;

    return match_count
}

function main(){
    const readline = require('readline-sync');

    const prizes = [0, 4, 7, 100, 50000, 1000000, 25000000];
    const winningTicket = pick6();
    const ticket_cost = 2;
    let expenses = 0;
    
    let playerTicket = pick6();
    
};

main();
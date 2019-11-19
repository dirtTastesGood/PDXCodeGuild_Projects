function pick6(){
    let ticket = [];

    for(let i=0; i<6; i++){
        ticket.push(Math.ceil(Math.random()*99));
    }

    return ticket
}

function countMatches(ticket, win){
    let winning_ticket = win.slice();
    // console.log(`ticket: ${ticket}\nwinning_ticket: ${winning_ticket}`);
    
    matches = 0;
    for(let i=0; i<ticket.length; i++){
        if(ticket[i] == winning_ticket[i]){
            matches++
        }
    }
    return matches
}

function main(){
    const readline = require('readline-sync');

    const prizes = [0, 4, 7, 100, 50000, 1000000, 25000000];
    const winning_ticket = pick6();
    const ticket_cost = 2;
    let expenses = 0;
    let winnings = 0;
    
    let turn_count = 0;
    while(turn_count < 100000){
        turn_count++;

        let player_ticket = pick6();
        expenses += ticket_cost;
        let matches = countMatches(player_ticket, winning_ticket);
        
        // console.log(matches);
        

        winnings += prizes[matches];
    }

    console.log(`You spent: $${expenses} and won $${winnings}.`);
    console.log((expenses - winnings) / expenses);
    
};

main();
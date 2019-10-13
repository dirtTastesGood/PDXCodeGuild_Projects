from random import randint

def buy_socks():
    sock_types = ['ankle', 'crew', 'calf', 'thigh']
    socks = {}   

    for sock in sock_types:
        socks[sock] = {}
        socks[sock] = {'quantity': 0, 'pairs':0, 'singles':0}

    i = 0
    while i < 100:
        sock_type = sock_types[randint(0, len(sock_types)-1)]
        socks[sock_type]['quantity'] += 1
        i += 1
    
    return socks
    
def pair_socks(socks):
    for sock in socks:
        for color in socks[sock]:
            
            socks[sock]['pairs'] = socks[sock]['quantity'] // 2
            socks[sock]['singles'] = socks[sock]['quantity'] % 2


    return socks        

def main():
    socks = buy_socks()

    #print(socks)

    pair_socks(socks)
    for sock in socks:
        print(f"{sock}: ")
        print(f"    quantity: {socks[sock]['quantity']}")
        print(f"        pairs: {socks[sock]['pairs']}\n        singles: {socks[sock]['singles']}")
        
main()
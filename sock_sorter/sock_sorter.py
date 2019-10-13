from random import randint

def buy_socks():
    sock_types = ['ankle', 'crew', 'calf', 'thigh']
    sock_colors = ['black', 'white', 'blue']
    socks = {}   

    for sock in sock_types:
        socks[sock] = {}
        for color in sock_colors:
            socks[sock][color] = {'quantity': 0, 'pairs':0, 'singles':0}

    i = 0
    while i < 100:
        sock_type = sock_types[randint(0, len(sock_types)-1)]
        sock_color = sock_colors[randint(0, len(sock_colors)-1)]
        socks[sock_type][sock_color]['quantity'] += 1
        i += 1
    
    return socks
    
def pair_socks(socks):
    for sock in socks:
        for color in socks[sock]:
            
            socks[sock][color]['pairs'] = socks[sock][color]['quantity'] // 2
            socks[sock][color]['singles'] = socks[sock][color]['quantity'] % 2


    return socks        

def main():
    socks = buy_socks()

    #print(socks)

    pair_socks(socks)
    for sock in socks:
        print(f"{sock}: ")
        for color in socks[sock]:
            print(f"    {color}:\n        quantity: {socks[sock][color]['quantity']}")
            print(f"            pairs: {socks[sock][color]['pairs']}\n            singles: {socks[sock][color]['singles']}")
        pass    
main()
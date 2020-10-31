def calculate_damage(your_type, opponent_type, attack, defense):
    effectiveness = {'firegrass':2,'firewater':0.5, 'fireelectric':1, 'watergrass':0.5, 'waterelectric':0.5, 'grasselectric':1, \
                     'grassfire':0.5, 'waterfire':2, 'electricfire':1, 'grasswater':2, 'electricwater':2, 'electricgrass':1, \
                     'electricelectric':0.5, 'waterwater':0.5, 'firefire':0.5, 'grassgrass':0.5}
    return 50*(attack/defense)*(effectiveness[your_type+opponent_type])

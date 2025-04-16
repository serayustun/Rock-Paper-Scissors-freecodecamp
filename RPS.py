import random

def player(prev_play, opponent_history=[], play_order={}, my_history=[]):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)

    # Başlangıç değeri
    my_move = 'R'

    # Kendi geçmişini güncelle
    my_history.append(my_move)

    prediction = 'P'

    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1

        potential_plays = [
            "".join([*opponent_history[-4:], v])
            for v in ['R', 'P', 'S']
        ]

        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    # Abbey için ezberi bozma (100 turda bir rastgele)
    if len(opponent_history) > 0 and len(opponent_history) % 100 == 0:
        prediction = random.choice(['R', 'P', 'S'])

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # prediction'ı geçerli bir karakterle sınırlayın
    if prediction in ideal_response:
        my_move = ideal_response[prediction]
    else:
        # Eğer prediction geçersizse, varsayılan olarak 'R' döndür
        my_move = 'R'

    return my_move

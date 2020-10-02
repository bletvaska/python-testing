from random import randint


def play_game(secret=13):
    print('Myslím si číslo od 1 do 20.')
    # secret = 13
    tip = None
    counter = 5

    while tip != secret and counter > 0:
        tip = input('Tvoj tip: ')
        tip = int(tip)
        counter -= 1

        if tip < secret:
            print(f'Hmm... Moje číslo je väčšie ako {tip}.')
        elif tip > secret:
            print(f'Hmm... Moje číslo je menšie ako {tip}.')
        else:
            print('Ta ty genius.')
            break
    else:
        print('Ta ty si lama. Ta si to neuhadol. Ta se zamisly.')


def main():
    # play_game(randint(1, 20))
    play_game(13)


if __name__ == '__main__':
    main()

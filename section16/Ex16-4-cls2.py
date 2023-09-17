'''
파일명 : Ex16-4-cls2.py
'''
class HoldemPlayer:
    card3 = ''
    card4 = ''
    card5 = ''
    card6 = ''
    card7 = ''

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def get_card_info(self):
        print(f'card1: {self.card1}')
        print(f'card2: {self.card2}')
        print(f'card3: {HoldemPlayer.card3}')
        print(f'card4: {HoldemPlayer.card4}')
        print(f'card5: {HoldemPlayer.card5}')
        print(f'card6: {HoldemPlayer.card6}')
        print(f'card7: {HoldemPlayer.card7}')

    @classmethod
    def set_card3(cls, card):
        cls.card3 = card

    @classmethod
    def set_card4(cls, card):
        cls.card4 = card

    @classmethod
    def set_card5(cls, card):
        cls.card5 = card

    @classmethod
    def set_card6(cls, card):
        cls.card6 = card

    @classmethod
    def set_card7(cls, card):
        cls.card7 = card

# 실행코드
player1 = HoldemPlayer('S-A', 'S-K')
player2 = HoldemPlayer('D-2', 'D-7')
player3 = HoldemPlayer('H-A', 'C-4')

print('1Round')
print('player1')
player1.get_card_info()
print('player2')
player2.get_card_info()

print('2Round')
HoldemPlayer.set_card3('D-K')
print('player1')
player1.get_card_info()
print('player2')
player2.get_card_info()


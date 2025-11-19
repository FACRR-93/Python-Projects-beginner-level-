import art, random, game_data

print(art.logo)
score = 0
game = True
A = random.randint(0,49)
B = random.randint(0,49)

def initial_display(optionA, optionB):
    print(f"Compare A: {game_data.data[optionA]['name']}, a {game_data.data[optionA]['description']}, from {game_data.data[optionA]['country']}.")
    print(art.vs)
    print(f"Against B: {game_data.data[optionB]['name']}, a {game_data.data[optionB]['description']}, from {game_data.data[optionB]['country']}.")

def compare(optionA, optionB):
    """Verifica qual das personalidades tem maior numero de seguidores e retorna qual"""
    if game_data.data[optionA]['follower_count'] > game_data.data[optionB]['follower_count']:
        return 'a'
    else:
        return 'b'

while game:

    initial_display(A,B)
    compare(A,B)
    choice = input("Who has more followers? Type 'A' or 'B' ").lower()

    if choice == compare(A,B):
        score += 1
        print("\n" * 50)
        print(art.logo)
        print(f"You're right! Current score: {score}")
        A = B
        B = random.randint(0,49)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False



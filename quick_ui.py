import streamlit as st
from classes.guessing_game import GuessingGame, RandomNumberGenerator

# Game setup
@st.cache_resource
def initialize_game():
    number_generator = RandomNumberGenerator()
    return GuessingGame(number_generator, attempt_limit=10)


# Streamlit app
st.title("Guess the Number Game")

# Initialize or retrieve the game
game = initialize_game()

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, value=50, step=1)
if st.button("Check your guess!"):
    result = game.check_guess(guess)
    st.write(result)

if game.end_condition():
    # end game. exit game!
    st.write("Game Over. Thank you for playing!")
    st.stop()  # This will stop the Streamlit app

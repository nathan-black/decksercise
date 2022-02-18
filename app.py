import streamlit as st
import random

st.title("🃏 Decksercise 🃏")
st.subheader("A random workout generator")
# Input number of cards
#sample_size = st.sidebar.slider(label="Choose the number of cards to pull", min_value=1, max_value=54, value=25, step=1)
rank =['Ace','King','Queen','Jack','2','3','4','5','6','7','8','9','10']
suit =['Hearts ♥️','Clubs ♣️','Diamonds ♦️','Spades ♠️']
suit_emojis = ["♥️", "♣️", "♦️", "♠️" ]
deck = [x + " of " + y for x in rank for y in suit] + ["Joker", "Joker"]
exercises = ['Push-ups', 'Sit-ups', 'Jumping jacks', 'Squats', "Sumo squats"]


if "selected_exercises" not in st.session_state:
    st.session_state.selected_exercises = random.sample(exercises, 4)

if "selected_cards" not in st.session_state:
    st.session_state.selected_cards = random.sample(deck, 26)

if st.button("Generate new exercises"):
    st.session_state.selected_exercises = random.sample(exercises, 4)


for i in range(len(suit)):
    st.write(f"{suit[i]} mean you're doing {st.session_state.selected_exercises[i]}")
st.write("Jokers 🃏 mean you're doing burpees")


if st.button("Pick a card") and len(st.session_state.selected_cards) > 0:
    selected_card = random.sample(st.session_state.selected_cards, 1)[0]
    st.session_state.selected_cards.remove(selected_card)
    st.write(selected_card)
    selected_rank = selected_card.split(' of')[0]
    reps = selected_rank
    if selected_rank != "Joker":
        selected_exercise = st.session_state.selected_exercises[suit.index(selected_card.split('of ')[1])]
        message = f"Do {reps} {selected_exercise}"
    if selected_rank in ["King", "Queen", "Jack"]:
        message = f"Do 10 {selected_exercise}"
    if selected_rank == "Ace":
        message = f"Do 11 {selected_exercise}"
    if selected_rank == "Joker":
        message = "Do 15 burpees"

    st.write(message)
    if len(st.session_state.selected_cards) > 0:
        st.write(f"{len(st.session_state.selected_cards)} to go!")

if len(st.session_state.selected_cards) < 1:
    st.write("Great job! You're done for today. See you tomorrow!!!")
    st.balloons()




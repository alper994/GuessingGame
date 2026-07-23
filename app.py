import streamlit as st
import random

st.title("🎯 Guessing Game: Read Alpi's Mind!")

GUESS_LIMIT = 3


# Spiel initialisieren
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

if "guess_number" not in st.session_state:
    st.session_state.guess_number = 0

if "game_finished" not in st.session_state:
    st.session_state.game_finished = False


# Eingabe
guess = st.number_input(
    "Guess a number between 1-100:",
    min_value=1,
    max_value=100,
    step=1
)


# Guess Button
if st.button("Guess"):

    if st.session_state.game_finished:
        st.warning("Game finished. Press Restart to play again.")

    else:
        st.session_state.guess_number += 1

        # Richtige Antwort
        if guess == st.session_state.secret_number:
            st.success(
                f"🎉 {guess} is correct! You win!"
            )
            st.session_state.game_finished = True


        # Letzter Versuch verloren
        elif st.session_state.guess_number >= GUESS_LIMIT:
            st.error(
                f"😢 You lose! The number was {st.session_state.secret_number}."
            )
            st.session_state.game_finished = True


        # Noch Versuche vorhanden
        elif guess > st.session_state.secret_number:
            st.warning(
                f"{guess} is too high! Try again."
            )


        else:
            st.warning(
                f"{guess} is too low! Try again."
            )


# Anzeige der Versuche
st.write(
    f"Attempts: {st.session_state.guess_number}/{GUESS_LIMIT}"
)


# Neustart
if st.button("🔄 Restart Game"):

    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guess_number = 0
    st.session_state.game_finished = False

    st.rerun()
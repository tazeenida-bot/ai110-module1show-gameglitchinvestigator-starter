from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# Bug fix tests: hint direction was reversed for guesses near the secret
def test_hint_too_high_near_secret():
    # Bug: guessing 70 when secret is 69 showed "Go Higher" instead of "Go Lower"
    outcome, _ = check_guess(70, 69)
    assert outcome == "Too High"

def test_hint_too_low_near_secret():
    # Bug: guessing 68 when secret is 69 showed "Go Lower" instead of "Go Higher"
    outcome, _ = check_guess(68, 69)
    assert outcome == "Too Low"

def test_hint_message_too_high():
    # The "Too High" message should direct the player to go lower
    _, message = check_guess(70, 69)
    assert "LOWER" in message

def test_hint_message_too_low():
    # The "Too Low" message should direct the player to go higher
    _, message = check_guess(68, 69)
    assert "HIGHER" in message

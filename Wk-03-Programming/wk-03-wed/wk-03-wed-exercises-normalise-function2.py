#Exercises Week 3 Wed

def normalise(text):
    print(f"text = {text}")
    print(f"text.strip() = {text.strip()}")
    print(f"text.rstrip() = {text.rstrip()}")
    print(f"text.lstrip() = {text.lstrip()}")

    text_stripped = text.strip()
    text_stripped_title = text_stripped.title()
    text_stripped_title_replace = text_stripped_title.replace("  ", " ")
    #printing step by step below
    print("\n")
    print(f"text_stripped = {text_stripped}")
    print(f"text_stripped_title = {text_stripped_title}")
    print(f"text_stripped_title_replace = {text_stripped_title_replace}")

normalise(" alice   smith   ")

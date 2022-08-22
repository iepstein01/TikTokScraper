def get_interests():
    interests = []
    while True:
        interest = input(
            'What are you interests? Please use single words, type "done" when finished.'
        )
        if interest == "done".lower():
            return interests
        interests.append(interest)

almaadrastu_mubaarakah = {
    "First Students": ["Qossim", "Abdulqoyyum"],
    "Last Students": ["Mustapa", "Hassan"]
}

almaadrastu_mubaarakah["Ustadh"] = ["Mubarak", "Abu Saalih"]
print(almaadrastu_mubaarakah["Ustadh"])
print(almaadrastu_mubaarakah)

almaadrastu_mubaarakah["Last Students"] = ["Mustapa", "Hassan", "Yussuf"]
print(almaadrastu_mubaarakah)


video_game_options = {}

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "medium"
video_game_options["volume"] = 7

print(video_game_options)


video_game_options["subtitles"] = False
video_game_options["difficulty"] = "Hard"
video_game_options["volume"] = 10

print(video_game_options)

words = ["danger", "beware", "beware", "beware", "beware", "danger"]

def counts_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1

        else:
            counts[word] = 1

    return counts

print(counts_words(words))







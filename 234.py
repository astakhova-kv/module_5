
def get_videos(key_word):
    new_videos = []
    videos = ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
    for i in range(len(videos)):
        list1 = videos[i].split()
        for j in list1:
            if key_word.casefold() in j.casefold():
                new_videos.append(videos[i])
    print(new_videos)




get_videos('ПрОг')
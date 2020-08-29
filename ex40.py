class Song (object):

    def __init__(self,lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["www www www www w ww www ",
                   "rr rrrr rr rrrrrr r rrr ",
                   "t tttt t ttttt ttt tt t t"])

bulls_on_parade = Song(["ooo ooooooo oooooooo oo o",
                        " yyy yyyyyy yyyyyy yyy yy",
                        " aaa aaa  aa a  aaaaa a a"])
                                                 
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

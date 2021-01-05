class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        name_dic = {self.name: None}
        temp = self.next
        while temp:
            if temp.name in name_dic:
                return True
            name_dic[temp.name] = None
            temp = temp.next
            
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
assert first.is_repeating_playlist() == True

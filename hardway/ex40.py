class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def singme(self):
        for line in self.lyrics:
            print(line)



        
happy_bday = song(["Paljon onnea vaan", 
                    "paljon onnea vaan"])
satu_sau = song(["Satu meni saunaan",
                "satu tuli saunasta"])

joulukuusi = ["Hoohhoo Joulu on taas",
            "Joulu on taas"]
            
joulupuu = song(joulukuusi)

playlist = [happy_bday, satu_sau, joulupuu]

for x in playlist:
    x.singme()
    
    

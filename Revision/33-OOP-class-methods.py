class colorpalete:
    def __init__(self, color1, color2, color3):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    @classmethod
    def auto_palete(cls, color1):
        s = 0
        for c in color1:
            s += c
        s = s/3
        color2 = [s, s, s]
        color3 = [s/2, s/2, s/2]
        return cls(color1, color2, color3)


palete1 = colorpalete([50, 200, 255], [100, 100, 100], [50, 25, 75]) 
print(palete1.color1, palete1.color2, palete1.color3)
palete2 = colorpalete.auto_palete([25, 100, 255]) 
print(palete2.color1, palete2.color2, palete2.color3)


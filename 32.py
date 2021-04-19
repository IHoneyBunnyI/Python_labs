class C32:
    this = 'A'
    def fade(self):
        if self.this == 'A':
            self.this = 'B'
            return 0
        elif self.this == 'B':
            self.this = 'C'
            return 1
        elif self.this == 'C':
            self.this = 'C'
            return 3
        elif self.this == 'D':
            self.this = 'D'
            return 5
        elif self.this == 'E':
            self.this = 'F'
            return 6
        else:
            raise RuntimeError
    def clone(self):
        if self.this == 'C':
            self.this = 'D'
            return 2
        elif self.this == 'D':
            self.this = 'E'
            return 4
        if self.this == 'E':
            self.this = 'C'
            return 7
        if self.this == 'F':
            self.this = 'B'
            return 8
        else:
            raise RuntimeError

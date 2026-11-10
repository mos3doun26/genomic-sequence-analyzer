class DNA:
    def __init__(self, sequence):
        self.sequence = sequence
        self.nucleotides = {}

    @property
    def nucleotides(self):
        ...

    def gc_content(self):
        ...

    def transcript(self):
        ...

    def translate(self):
        ...

    def orfs(self):
        ...

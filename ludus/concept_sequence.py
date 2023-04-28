from ludus.models.concept import Concept


class ConceptSequence(Concept):
    def __init__(self):
        self.program = []
        self.commands = ["walk()", "jump()"]
        self.board = [['-' for _ in range(5)] for _ in range(5)]

from ludus.models.concept import Concept


class ConceptSequence(Concept):
    def get_commands(self) -> list:
        return ["walk()", "walk()", "jump()", "walk()"]

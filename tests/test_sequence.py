from ludus.concept_sequence import ConceptSequence


def test_setup():
    sequence = ConceptSequence()
    assert len(sequence.board) == 5
    assert len(sequence.commands) == 2
    assert len(sequence.program) == 0

from ludus.concept_sequence import ConceptSequence


def test_flow():
    sequence = ConceptSequence()
    assert len(sequence.get_commands()) == 4

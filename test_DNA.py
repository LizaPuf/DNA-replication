from main import dna
import pytest

@pytest.mark.parametrize('dna_sequence, dna_second_sequence', [('AATTAAT', 'TTAATTA'),
                                                               ('TATA', 'ATAT'),
                                                               ('AGTG', 'TCAC')])
def test_dna_replication(dna_sequence, dna_second_sequence):
    assert dna(dna_sequence) == dna_second_sequence

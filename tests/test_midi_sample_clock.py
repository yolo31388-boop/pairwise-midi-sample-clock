import pytest
import media.midi_sample_clock as mod

CASES = [
    ("tick_to_sample", (1,)),
    ("loop_note_off", (1,)),
    ("program_defer", (1,)),
    ("port_serial", (1,)),
    ("resume_flush", (1,)),
    ("determinism", (1,)),
    ("monotonic_event", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("tempo_map", (1,)),
    ("metrics", (1,)),
    ("schedule", (1,)),
    ("note_on", (1,)),
    ("note_off", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

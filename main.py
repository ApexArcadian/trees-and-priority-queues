
from triage_system import TriageSystem


# Test Hospital Emergency Room Triage System
def test_triage_system():
    """Test the triage system with sample patient data."""
    triage = TriageSystem()
    
    # Add patients in the order they arrive
    patients = [
        ("Sofia", 5),
        ("Bob", 2),
        ("Charlie", 4),
        ("Diana", 3),
        ("Eli", 1),
        ("Tom", 4),
        ("Alice", 5),
        ("Rachel", 4),
    ]
    
    print("=== Hospital Emergency Room Triage System ===\n")
    print(f"Adding {len(patients)} patients...\n")
    
    for name, severity in patients:
        triage.AddPatient(name, severity)
        print(f"Arrival: {name} (Severity {severity})")
    
    print(f"\nQueue size: {triage.Size()}")
    print(f"Queue is empty: {triage.IsEmpty()}\n")
    
    print("--- Processing patients (highest severity first) ---\n")
    
    while not triage.IsEmpty():
        patient = triage.ProcessNext()
        name, severity = patient
        print(f"Now treating: {name} (Severity {severity})")
    
    print(f"\nFinal queue size: {triage.Size()}")
    print(f"Queue is empty: {triage.IsEmpty()}")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n=== Edge Case Testing ===\n")
    
    triage = TriageSystem()
    
    # Test empty queue operations
    print("1. Empty queue operations:")
    print(f"   ProcessNext on empty: {triage.ProcessNext()}")
    print(f"   PeekNext on empty: {triage.PeekNext()}")
    print(f"   IsEmpty: {triage.IsEmpty()}")
    print(f"   Size: {triage.Size()}\n")
    
    # Test PeekNext
    print("2. PeekNext without removal:")
    triage.AddPatient("Emergency", 5)
    print(f"   After adding Emergency (5)...")
    print(f"   PeekNext: {triage.PeekNext()}")
    print(f"   PeekNext again (same): {triage.PeekNext()}")
    print(f"   Size still: {triage.Size()}\n")
    
    # Test Clear
    print("3. Clear operation:")
    triage.Clear()
    print(f"   After Clear(), IsEmpty: {triage.IsEmpty()}")
    print(f"   Size: {triage.Size()}\n")
    
    # Test invalid inputs
    print("4. Invalid input handling:")
    try:
        triage.AddPatient("", 3)
    except ValueError as e:
        print(f"   Empty name rejected: {e}")
    
    try:
        triage.AddPatient("Valid", 6)
    except ValueError as e:
        print(f"   Severity 6 rejected: {e}")
    
    try:
        triage.AddPatient("Valid", 0)
    except ValueError as e:
        print(f"   Severity 0 rejected: {e}")


if __name__ == "__main__":
    test_triage_system()
    test_edge_cases()
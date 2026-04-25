import heapq


class TriageSystem:
    """
    Hospital Emergency Room Triage System.
    
    Maintains a priority queue of patients, ordered by severity (higher=more urgent)
    with ties broken by arrival order (FIFO).
    """
    
    _arrival_counter = 0  # Class-level counter for arrival order
    
    def __init__(self):
        """Initialize an empty triage system."""
        self._queue = []  # Min-heap (using negative severity for max-heap behavior)
        self._size = 0
    
    @staticmethod
    def NextArrivalOrder():
        """
        Return the current arrival order and advance the counter.
        
        This is a class-level method that tracks the order in which patients arrive,
        used for tie-breaking when severities are equal.
        """
        order = TriageSystem._arrival_counter
        TriageSystem._arrival_counter += 1
        return order
    
    def AddPatient(self, name, severity):
        """
        Add a new patient to the triage queue.
        
        Pre: name is nonempty; 1 <= severity <= 5
        Post: Patient inserted with priority by severity (high first) then arrival order.
        
        Args:
            name: Patient's name (must be nonempty string)
            severity: Severity level (must be int in [1, 5])
            
        Raises:
            ValueError: If name is empty or severity is outside [1, 5]
        """
        # Validate inputs
        if not name or not isinstance(name, str):
            raise ValueError("Patient name must be a nonempty string")
        if not isinstance(severity, int) or severity < 1 or severity > 5:
            raise ValueError("Severity must be an integer between 1 and 5")
        
        # Get arrival order for tie-breaking
        arrival_order = TriageSystem.NextArrivalOrder()
        
        # Push to heap: (-severity, arrival_order, name)
        # Negative severity converts min-heap to max-heap behavior
        heapq.heappush(self._queue, (-severity, arrival_order, name))
        self._size += 1
    
    def ProcessNext(self):
        """
        Remove and return the highest-priority patient.
        
        Post: If nonempty, removes max-priority patient and returns (name, severity).
              If empty, returns None. Size decreases by 1 on removal.
              
        Returns:
            Tuple (name, severity) of next patient to treat, or None if queue empty.
        """
        if self.IsEmpty():
            return None
        
        neg_severity, arrival_order, name = heapq.heappop(self._queue)
        self._size -= 1
        severity = -neg_severity  # Convert back from negative
        
        return (name, severity)
    
    def PeekNext(self):
        """
        Return (without removing) the next patient to be processed.
        
        Post: If nonempty, returns (name, severity) of top patient without modification.
              If empty, returns None. Queue unchanged.
              
        Returns:
            Tuple (name, severity) of next patient to treat, or None if queue empty.
        """
        if self.IsEmpty():
            return None
        
        neg_severity, arrival_order, name = self._queue[0]
        severity = -neg_severity
        
        return (name, severity)
    
    def IsEmpty(self):
        """
        Check if the triage system is empty.
        
        Post: Returns True iff queue contains no patients; otherwise False.
        
        Returns:
            Boolean indicating if queue is empty.
        """
        return self._size == 0
    
    def Size(self):
        """
        Return the number of patients in the system.
        
        Post: Returns count of patients currently queued.
        
        Returns:
            Integer count of patients.
        """
        return self._size
    
    def Clear(self):
        """
        Remove all patients from the system.
        
        Post: Queue becomes empty; size becomes 0. Arrival counter not reset.
        """
        self._queue = []
        self._size = 0

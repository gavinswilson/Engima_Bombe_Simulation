class streamTester:
    def __init__(self, mode="digits"):
        """
        Configures the tracker based on the desired character set.
        Modes: 'digits', 'upper', 'alpha', 'binary', 'ascii', or a custom list.
        """
        if mode == "digits":
            self.chars = [str(i) for i in range(10)]
        elif mode == "upper":
            self.chars = [chr(i) for i in range(65, 91)]
        elif mode == "alpha":
            self.chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        elif mode == "alphanumeric":
            self.chars = [chr(i) for i in range(48, 123)] 
        elif mode == "binary":
            self.chars = ["0", "1"]
        elif mode == "ascii":
            self.chars = [chr(i) for i in range(128)]
        elif isinstance(mode, list):
            self.chars = mode
        else:
            raise ValueError("Unknown mode selected.")

        # Initialize matrix with 0 for all expected characters
        self.matrix = {char: 0 for char in self.chars}
        self.total_processed = 0
        self.others = 0

    def disto(self, item):
        """
        Accepts a digit or character, converts to string, and updates matrix.
        """
        key = str(item)
        if key in self.matrix:
            self.matrix[key] += 1
        else:
            self.others += 1
        self.total_processed += 1

    def print_matrix(self):
        """
        Prints the frequency distribution. 
        Note: For large sets like ASCII, this filters for items with counts > 0.
        """
        print(f"\n--- Distribution Matrix (Total: {self.total_processed}) ---")
        print(f"{'Char':<10} | {'Count':<10} | {'Percentage'}")
        print("-" * 40)
        
        # Sort by count descending for better readability
        sorted_items = sorted(self.matrix.items(), key=lambda x: x[1], reverse=True)
        
        for char, count in sorted_items:
            if count > 0: # Only show what we actually found
                percentage = (count / self.total_processed * 100)
                # Escape newlines or tabs for ASCII display
                display_char = repr(char) if len(char) == 1 else char
                print(f"{display_char:<10} | {count:<10} | {percentage:.2f}%")
        
        if self.others > 0:
            print(f"{'Unmapped':<10} | {self.others:<10} | {(self.others/self.total_processed*100):.2f}%")
        print("-" * 40)





def pi_spigot(count):
    """
    A generator that yields digits of pi using a spigot algorithm.
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    digits_found = 0
    
    while digits_found < count:
        if 4 * q + r - t < n * t:
            yield n
            digits_found += 1
            nr = 10 * (r - n * t)
            n  = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r  = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n  = nn
            r  = nr

def randomCharacterGenerator(count):
    """
    A generator that yields random ASCII characters.
    """
    import random
    for _ in range(count):
        yield chr(random.randint(0, 127))

def run_pi_processing(count):
    """
    Iterates through the spigot and calls disto() for each digit.
    """

    # --- Execution ---
    tracker = streamTester("digits")


    for digit in pi_spigot(count):
        tracker.disto(digit)

    tracker.print_matrix()

def run_ascii_stream(count):
    """
    Iterates through the a list of chars and calls disto() for each ascii number.
    """

    # --- Execution ---
    tracker = streamTester("ascii")


    for digit in randomCharacterGenerator(count):
        tracker.disto(digit)

    tracker.print_matrix()

# Example: Run for the first 15 digits
# run_pi_processing(150000)
run_ascii_stream(1500000)




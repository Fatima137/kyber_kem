class Params:
    # Adjust these values based on the Kyber variant you're working with
    KYBER_N = 256  # Degree of the polynomial (change for Kyber768 and Kyber1024)
    KYBER_Q = 3329  # Modulus (change for Kyber768 and Kyber1024)
    KYBER_SYMBYTES = 32
    KYBER_POLYBYTES = 384
    KYBER_INDCPA_BYTES = 800
    KYBER_ETA = 2
    KYBER_K = 2  # Number of polynomials in the vector (Kyber512)

    # Root of unity for NTT (change based on variant)
    KYBER_ROOT = 4  # Example for Kyber512 (change for Kyber768 or Kyber1024)

    def __init__(self):
        self.polyvec_bytes = self.KYBER_K * self.KYBER_POLYBYTES
        self.ntt_size = self.KYBER_N  # This is the size of the polynomial for NTT
        self.ntt_modulus = self.KYBER_Q  # Modulus for the NTT
        self.ntt_root = self.KYBER_ROOT  # Root of unity for NTT

    # Additional methods to compute NTT can be added here

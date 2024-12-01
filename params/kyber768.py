class Params:
    KYBER_N = 256
    KYBER_Q = 3329
    KYBER_SYMBYTES = 32
    KYBER_POLYBYTES = 384
    KYBER_INDCPA_BYTES = 800
    KYBER_K = 3  # For Kyber768

    def __init__(self):
        self.polyvec_bytes = self.KYBER_K * self.KYBER_POLYBYTES

import random

def generate_otp(length=4):
    if length <= 0:
        raise ValueError("OTP length must be positive.")
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

# Example usage
otp = generate_otp()  # default 4-digit OTP
print("Your OTP is:", otp)
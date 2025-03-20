import math

def calculate_fos(phi_deg, theta_deg, psi_deg, H, c, gamma):
    

    phi = math.radians(phi_deg)
    theta = math.radians(theta_deg)
    psi = math.radians(psi_deg)
    
    
    A = H / math.cos(psi)
    
    
    W = gamma * A
    
    
    R = (W * math.cos(theta) * math.tan(phi)) + (c * A)
    
    
    D = W * math.sin(theta)
    
    
    if D == 0:
        return float('inf')  
    FOS = R / D
    return FOS

def main():
    print("Rock Slope Stability Factor of Safety (FOS) Calculator")
    try:
        phi_deg = float(input("Enter friction angle (φ) in degrees: "))
        theta_deg = float(input("Enter slope angle (θ) in degrees: "))
        psi_deg = float(input("Enter joint angle (ψ) in degrees: "))
        H = float(input("Enter height of bench (H) in meters: "))
        c = float(input("Enter cohesion (c): "))
        gamma = float(input("Enter unit weight of rock (γ) in kN/m³: "))
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values.")
        return

    fos = calculate_fos(phi_deg, theta_deg, psi_deg, H, c, gamma)
    print(f"\nThe calculated Factor of Safety (FOS) is: {fos:.2f}")

if __name__ == "__main__":
    main()

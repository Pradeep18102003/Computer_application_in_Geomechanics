def calculate_pillar_strength_and_FOS():
    """
    This script asks:
      1. Which pillar strength formula to use.
      2. Whether the pillar is square or rectangular.
    Then it collects the necessary inputs:
      - For both formulas: pillar height (h), overburden depth (H), and center-to-center pillar spacing (s).
      - For Formula #1: UCS (sigma_c) and pillar effective width (w).
      - For Formula #2: pillar effective width (w) is used in the formula.
      - For pillar geometry: if square, pillar width (w) is used; if rectangular, both width (w) and length (l) are input.
    It then computes:
      1. Pillar Strength (S_p) using the chosen formula.
      2. Pillar Stress using Tributary Area Theory.
      3. Factor of Safety = S_p / (pillar stress).
    """

    # First, ask the user about the pillar shape.
    print("Is the pillar square or rectangular?")
    pillar_shape = input("Enter 'square' or 'rectangular': ").strip().lower()
    w_g = float(input("Enter the width of gallery in meters: "))

    if pillar_shape == "square":
        # For a square pillar, ask for the width.
        w = float(input("Enter the pillar width (w) in meters: "))
        pillar_area = w ** 2
        centre_to_centre = (w+w_g/2)**2
    elif pillar_shape == "rectangular":
        # For a rectangular pillar, ask for both width and length.
        w = float(input("Enter the pillar effective width (w) in meters (used in strength formula): "))
        l = float(input("Enter the pillar length (l) in meters: "))
        pillar_area = w * l
        centre_to_centre = (w+w_g/2) * (l+w_g/2)
    else:
        print("Invalid pillar shape. Please run the program again and enter 'square' or 'rectangular'.")
        return

    # Next, choose the strength formula.
    print("\nChoose the formula for pillar strength calculation:")
    print("1) Formula 1:")
    print("   S_p = 0.27 * sigma_c * h^(-0.36) + (1 + H/250)*((w/h) - 1),  [MPa]")
    print("2) Formula 2:")
    print("   S_p = K * (w/h)^alpha * (h)^beta,  [MPa after conversion]")
    formula_choice = input("Enter '1' or '2': ").strip()

    # Common inputs for both formulas.
    h = float(input("Enter pillar height (h) in meters: "))
    H = float(input("Enter overburden depth (H) in meters: "))
    

    if formula_choice == '1':
        # ------------------------------
        # FORMULA #1
        # S_p = 0.27 * sigma_c * h^(-0.36) + (1 + H/250) * ((w/h) - 1)
        # ------------------------------
        sigma_c = float(input("Enter UCS (sigma_c) in MPa: "))

        part1 = 0.27 * sigma_c * (h ** -0.36)
        part2 = (1 + (H / 250.0)) * ((w / h) - 1.0)
        S_p = part1 + part2  # Pillar strength in MPa

    elif formula_choice == '2':
        # ------------------------------
        # FORMULA #2 (Indian coal example)
        # S_p = K * (w/h)^alpha * (h)^beta
        # Using Jharia coalfield constants: K=260 psi, alpha=0.46, beta=0.66
        # Convert K from psi to MPa: 1 psi ≈ 0.00689476 MPa
        # ------------------------------
        K_psi = 260.0
        K_MPa = K_psi * 0.00689476  # ~1.7926 MPa
        alpha = 0.46
        beta = 0.66

        S_p = K_MPa * ((w / h) ** alpha) * (h ** beta)
    else:
        print("Invalid formula choice! Please run again and enter '1' or '2'.")
        return

    # Compute stress using Tributary Area Theory:
    # Overburden stress gradient = 0.025 MPa/m is assumed.
    # Pillar stress = (0.025 * H) * (tributary area / pillar cross-sectional area)
    # For tributary area, we use s^2.
    stress_pillar = 0.025 * H * (centre_to_centre / pillar_area)  # MPa

    # Factor of Safety (FoS)
    fos = S_p / stress_pillar if stress_pillar != 0 else 0

    # Print results
    print("\n--- RESULTS ---")
    print(f"Pillar Strength (S_p):  {S_p:.4f} MPa")
    print(f"Pillar Stress:          {stress_pillar:.4f} MPa")
    print(f"Factor of Safety (FoS): {fos:.4f}")


# --- RUN THE FUNCTION ---
if __name__ == "__main__":
    calculate_pillar_strength_and_FOS()

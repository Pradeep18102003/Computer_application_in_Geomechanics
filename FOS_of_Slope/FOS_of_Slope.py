import math

def tributary_area_stress(density, gravity, depth, wp, wg):
    density = density * 10**3  # Convert g/cm³ to kg/m³
    return (density * gravity * depth * (wp ** 2)) / ((wp - wg) ** 2)

def obert_duvall_strength(c1, w, h):
    c1 = c1 * 10**6  # Convert MPa to Pa
    return c1 * (0.778 + 0.222 * (w / h))

def holland_gaddy_strength(k, w, h):
    return k * math.sqrt(w / h)

def salamon_strength(w, h):
    return 1320 * (w ** 0.46) / (h ** 0.66)

def bieniawski_strength(sigma1, w, h):
    sigma1 = sigma1 * 10**6  # Convert MPa to Pa
    return sigma1 * (0.64 + 0.36 * (w / h))

def factor_of_safety(stress, strength):
    return strength / stress

def remark(fos):
    if fos >= 1.8:
        return "Safe"
    elif 1.3 <= fos < 1.8:
        return "Moderately Safe"
    else:
        return "Unsafe"

def main():
    print("Select the method to calculate pillar stress:")
    print("1. Tributary Area Theory")
    stress_method = int(input("Enter the method number: "))
    
    if stress_method == 1:
        density = float(input("Enter average density of overlying strata (g/cm^3): "))
        gravity = 9.81  # m/s^2
        depth = float(input("Enter depth of the coal seam (m): "))
        pillar_width = float(input("Enter pillar width (m): "))
        gallery_width = float(input("Enter gallery width (m): "))
        
        wp = pillar_width + gallery_width  # Corrected center-to-center pillar width
        wg = gallery_width
        
        stress = tributary_area_stress(density, gravity, depth, wp, wg)
    else:
        print("Invalid selection!")
        return
    
    print("Select the method to calculate pillar strength:")
    print("1. Obert-Duvall Formula: UCS * (0.778 + 0.222 * (w / h))")
    print("2. Holland-Gaddy Formula: k * sqrt(w / h)")
    print("3. Salamon Formula: 1320 * (w^0.46) / (h^0.66)")
    print("4. Bieniawski Formula: (cubical coal strength) * (0.64 + 0.36 * (w / h))")
    strength_method = int(input("Enter the method number: "))

    h = float(input("Enter pillar height (m): "))
    
    if strength_method == 1:
        c1 = float(input("Enter uniaxial compressive strength (MPa): "))
        strength = obert_duvall_strength(c1, wp, h)
    elif strength_method == 2:
        k = float(input("Enter K factor from lab tests: "))
        strength = holland_gaddy_strength(k, wp, h)
    elif strength_method == 3:
        strength = salamon_strength(wp, h)
    elif strength_method == 4:
        sigma1 = float(input("Enter strength of cubical coal specimen (MPa): "))
        strength = bieniawski_strength(sigma1, wp, h)
    else:
        print("Invalid selection!")
        return
    
    fos = factor_of_safety(stress, strength)
    fos_remark = remark(fos)

    stress = stress / 10**6  # Convert Pa to MPa
    strength = strength / 10**6  # Convert Pa to MPa
    
    print(f"\nPillar Stress: {stress:.2f} MPa")
    print(f"Pillar Strength: {strength:.2f} MPa")
    print(f"Factor of Safety: {fos:.2f}")
    print(f"Remark: {fos_remark}")

if __name__ == "__main__":
    main()

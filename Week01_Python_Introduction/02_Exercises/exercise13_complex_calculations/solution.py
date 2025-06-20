"""
Exercise 13: Complex Calculations - Complete Solution

This file demonstrates advanced mathematical calculations across multiple domains:
- Advanced Mathematics
- Scientific Calculations  
- Financial Mathematics
- Statistical Analysis
- Engineering Calculations

Using only Week 1 Python concepts with mathematical formulas.
"""

import math

def module1_advanced_mathematics():
    """Module 1: Toán học nâng cao"""
    print("=== ADVANCED MATHEMATICS ===")
    
    # 1. Phương trình bậc 2: ax² + bx + c = 0
    def solve_quadratic(a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"Two solutions: x1 = {x1:.3f}, x2 = {x2:.3f}"
        elif discriminant == 0:
            x = -b / (2*a)
            return f"One solution: x = {x:.3f}"
        else:
            return "No real solutions"
    
    print("1. Quadratic Equation (2x² - 7x + 3 = 0):")
    result = solve_quadratic(2, -7, 3)
    print(f"   {result}")
    
    # 2. Ma trận 2x2 determinant
    def matrix_2x2_determinant(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    matrix_2x2 = [[3, 2], [1, 4]]
    det = matrix_2x2_determinant(matrix_2x2)
    print(f"\n2. Matrix 2x2 Determinant {matrix_2x2}: {det}")
    
    # 3. Ma trận 3x3 determinant
    def matrix_3x3_determinant(matrix):
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    
    matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
    det_3x3 = matrix_3x3_determinant(matrix_3x3)
    print(f"3. Matrix 3x3 Determinant: {det_3x3}")
    
    # 4. Chuỗi sin approximation (Taylor series)
    def sin_approximation(x, terms=10):
        result = 0
        for n in range(terms):
            sign = (-1) ** n
            numerator = x ** (2*n + 1)
            denominator = math.factorial(2*n + 1)
            result += sign * numerator / denominator
        return result
    
    x = math.pi / 4  # 45 degrees
    sin_approx = sin_approximation(x)
    sin_actual = math.sin(x)
    print(f"4. Sin({x:.3f}) approximation: {sin_approx:.6f}, actual: {sin_actual:.6f}")
    
    # 5. Tích phân số (Trapezoidal rule)
    def trapezoidal_integration(func, a, b, n=1000):
        h = (b - a) / n
        result = (func(a) + func(b)) / 2
        for i in range(1, n):
            x = a + i * h
            result += func(x)
        return result * h
    
    # Integrate x² from 0 to 2
    def square_function(x):
        return x ** 2
    
    integral = trapezoidal_integration(square_function, 0, 2)
    exact = (2**3 - 0**3) / 3  # Exact integral of x²
    print(f"5. ∫x² dx from 0 to 2: {integral:.6f}, exact: {exact:.6f}")

def module2_scientific_calculations():
    """Module 2: Tính toán khoa học"""
    print("\n=== SCIENTIFIC CALCULATIONS ===")
    
    # 6. Ideal Gas Law: PV = nRT
    def ideal_gas_pressure(n, R, T, V):
        return (n * R * T) / V
    
    n = 2.5  # moles
    R = 8.314  # J/(mol·K)
    T = 298  # K (25°C)
    V = 0.5  # m³
    pressure = ideal_gas_pressure(n, R, T, V)
    print(f"6. Ideal Gas Pressure: {pressure:.2f} Pa")
    
    # 7. Kinetic Energy: KE = ½mv²
    def kinetic_energy(mass, velocity):
        return 0.5 * mass * velocity ** 2
    
    mass = 10  # kg
    velocity = 25  # m/s
    ke = kinetic_energy(mass, velocity)
    print(f"7. Kinetic Energy: {ke:.2f} J")
    
    # 8. Wave frequency: f = v/λ
    def wave_frequency(velocity, wavelength):
        return velocity / wavelength
    
    c = 3e8  # speed of light
    wavelength = 500e-9  # 500 nm
    frequency = wave_frequency(c, wavelength)
    print(f"8. Wave Frequency: {frequency:.2e} Hz")
    
    # 9. pH calculation: pH = -log₁₀[H⁺]
    def calculate_ph(h_concentration):
        return -math.log10(h_concentration)
    
    h_conc = 1e-7  # M
    ph = calculate_ph(h_conc)
    print(f"9. pH of solution: {ph:.2f}")
    
    # 10. Unit conversion: Energy (Joules to calories)
    def joules_to_calories(joules):
        return joules / 4.184
    
    energy_j = 1000  # J
    energy_cal = joules_to_calories(energy_j)
    print(f"10. Energy conversion: {energy_j} J = {energy_cal:.2f} cal")

def module3_financial_mathematics():
    """Module 3: Toán học tài chính"""
    print("\n=== FINANCIAL MATHEMATICS ===")
    
    # 11. Compound Interest với frequency khác nhau
    def compound_interest(principal, rate, time, frequency=1):
        amount = principal * (1 + rate/frequency) ** (frequency * time)
        return amount
    
    principal = 10000
    rate = 0.06  # 6%
    time = 5
    
    annual = compound_interest(principal, rate, time, 1)
    monthly = compound_interest(principal, rate, time, 12)
    daily = compound_interest(principal, rate, time, 365)
    
    print(f"11. Compound Interest on ${principal}:")
    print(f"    Annual: ${annual:.2f}")
    print(f"    Monthly: ${monthly:.2f}")
    print(f"    Daily: ${daily:.2f}")
    
    # 12. Annuity calculation
    def annuity_future_value(payment, rate, periods):
        if rate == 0:
            return payment * periods
        return payment * ((1 + rate) ** periods - 1) / rate
    
    payment = 1000  # monthly payment
    rate = 0.005   # 0.5% monthly
    periods = 60   # 5 years
    
    fv = annuity_future_value(payment, rate, periods)
    print(f"12. Annuity Future Value: ${fv:.2f}")
    
    # 13. Loan Payment (PMT)
    def loan_payment(principal, rate, periods):
        if rate == 0:
            return principal / periods
        return principal * (rate * (1 + rate) ** periods) / ((1 + rate) ** periods - 1)
    
    loan_amount = 200000  # $200k
    annual_rate = 0.04    # 4%
    years = 30
    monthly_rate = annual_rate / 12
    total_payments = years * 12
    
    monthly_payment = loan_payment(loan_amount, monthly_rate, total_payments)
    print(f"13. Monthly Loan Payment: ${monthly_payment:.2f}")
    
    # 14. Break-even analysis
    def break_even_point(fixed_costs, price_per_unit, variable_cost_per_unit):
        contribution_margin = price_per_unit - variable_cost_per_unit
        return fixed_costs / contribution_margin
    
    fixed_costs = 50000
    price = 25
    variable_cost = 15
    
    break_even = break_even_point(fixed_costs, price, variable_cost)
    print(f"14. Break-even Point: {break_even:.0f} units")
    
    # 15. ROI calculation
    def calculate_roi(gain, cost):
        return ((gain - cost) / cost) * 100
    
    investment_cost = 10000
    investment_gain = 12500
    roi = calculate_roi(investment_gain, investment_cost)
    print(f"15. ROI: {roi:.2f}%")

def module4_statistical_analysis():
    """Module 4: Phân tích thống kê"""
    print("\n=== STATISTICAL ANALYSIS ===")
    
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 16. Mean
    mean = sum(dataset) / len(dataset)
    print(f"16. Mean: {mean:.2f}")
    
    # 17. Median
    sorted_data = sorted(dataset)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2-1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    print(f"17. Median: {median:.2f}")
    
    # 18. Mode (simple implementation)
    def find_mode(data):
        frequency = {}
        for value in data:
            frequency[value] = frequency.get(value, 0) + 1
        max_freq = max(frequency.values())
        modes = [k for k, v in frequency.items() if v == max_freq]
        return modes[0] if len(modes) == 1 else modes
    
    mode = find_mode(dataset)
    print(f"18. Mode: {mode}")
    
    # 19. Standard Deviation
    variance = sum((x - mean) ** 2 for x in dataset) / len(dataset)
    std_dev = math.sqrt(variance)
    print(f"19. Standard Deviation: {std_dev:.3f}")
    
    # 20. Correlation coefficient (Pearson)
    def correlation(x, y):
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)) * 
                               sum((y[i] - mean_y) ** 2 for i in range(n)))
        
        return numerator / denominator if denominator != 0 else 0
    
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 6, 8, 10]
    corr = correlation(x_data, y_data)
    print(f"20. Correlation: {corr:.3f}")

def module5_engineering_calculations():
    """Module 5: Tính toán kỹ thuật"""
    print("\n=== ENGINEERING CALCULATIONS ===")
    
    # 21. Beam deflection (simple)
    def beam_deflection(load, length, modulus, moment_inertia):
        # Simple beam with point load at center
        return (load * length ** 3) / (48 * modulus * moment_inertia)
    
    load = 1000  # N
    length = 2   # m
    modulus = 200e9  # Pa
    moment_inertia = 1e-6  # m⁴
    
    deflection = beam_deflection(load, length, modulus, moment_inertia)
    print(f"21. Beam Deflection: {deflection*1000:.3f} mm")
    
    # 22. Fluid flow (Bernoulli's equation)
    def fluid_velocity(pressure_diff, density):
        return math.sqrt(2 * pressure_diff / density)
    
    pressure_diff = 5000  # Pa
    density = 1000  # kg/m³
    velocity = fluid_velocity(pressure_diff, density)
    print(f"22. Fluid Velocity: {velocity:.2f} m/s")
    
    # 23. Heat transfer
    def heat_transfer_rate(k, area, temp_diff, thickness):
        return k * area * temp_diff / thickness
    
    k = 50  # thermal conductivity W/(m·K)
    area = 2  # m²
    temp_diff = 100  # K
    thickness = 0.1  # m
    
    heat_rate = heat_transfer_rate(k, area, temp_diff, thickness)
    print(f"23. Heat Transfer Rate: {heat_rate:.0f} W")
    
    # 24. Electrical power
    def electrical_power(voltage, current, resistance=None):
        if resistance:
            return voltage ** 2 / resistance
        return voltage * current
    
    voltage = 120  # V
    current = 10   # A
    power = electrical_power(voltage, current)
    print(f"24. Electrical Power: {power:.0f} W")
    
    # 25. Efficiency calculation
    def efficiency(output, input_power):
        return (output / input_power) * 100
    
    output_power = 800  # W
    input_power = 1000  # W
    eff = efficiency(output_power, input_power)
    print(f"25. Efficiency: {eff:.1f}%")

def main_menu():
    """Menu chính cho tất cả modules"""
    while True:
        print("\n" + "="*50)
        print("=== COMPLEX CALCULATIONS ===")
        print("1. Advanced Mathematics")
        print("2. Scientific Calculations")
        print("3. Financial Mathematics")
        print("4. Statistical Analysis")
        print("5. Engineering Calculations")
        print("6. Run All Modules")
        print("7. Exit")
        
        choice = input("\nChọn module (1-7): ")
        
        if choice == "1":
            module1_advanced_mathematics()
        elif choice == "2":
            module2_scientific_calculations()
        elif choice == "3":
            module3_financial_mathematics()
        elif choice == "4":
            module4_statistical_analysis()
        elif choice == "5":
            module5_engineering_calculations()
        elif choice == "6":
            module1_advanced_mathematics()
            module2_scientific_calculations()
            module3_financial_mathematics()
            module4_statistical_analysis()
            module5_engineering_calculations()
        elif choice == "7":
            print("Cảm ơn bạn đã sử dụng Complex Calculations!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")

# Chạy chương trình chính
if __name__ == "__main__":
    main_menu()

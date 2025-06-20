# Hướng dẫn Exercise 13: Tính toán phức tạp

## Tổng quan

Bài tập này áp dụng Python để giải quyết các bài toán tính toán phức tạp trong nhiều lĩnh vực khác nhau. Bạn sẽ học cách implement mathematical formulas, xử lý precision, và organize code cho scientific computing.

## Chuẩn bị

Đảm bảo bạn đã nắm vững:

- Mathematical operators và functions
- `math` module và các built-in functions
- List operations và matrix representation
- String formatting cho output
- Error handling cho mathematical operations
- Function design và modularity

## Module 1: Toán học nâng cao

### Phương trình bậc 2

```python
import math

def solve_quadratic(a, b, c):
    """
    Giải phương trình ax² + bx + c = 0
    Returns: (x1, x2, discriminant) hoặc None nếu không có nghiệm thực
    """
    if a == 0:
        if b == 0:
            return None if c != 0 else "Infinite solutions"
        return (-c/b, None, None)  # Linear equation

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None  # No real solutions
    elif discriminant == 0:
        x = -b / (2*a)
        return (x, x, discriminant)
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return (x1, x2, discriminant)

# Usage example
a, b, c = 2, -5, 2
result = solve_quadratic(a, b, c)
if result:
    x1, x2, disc = result
    print(f"Phương trình: {a}x² + {b}x + {c} = 0")
    print(f"Nghiệm 1: x₁ = {x1}")
    print(f"Nghiệm 2: x₂ = {x2}")
    print(f"Discriminant: {disc}")
```

### Hình học phức tạp

```python
import math

def polygon_area(vertices):
    """
    Tính diện tích đa giác sử dụng Shoelace formula
    vertices: list of (x, y) tuples
    """
    n = len(vertices)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    return abs(area) / 2

def truncated_cone_volume(r1, r2, height):
    """
    Tính thể tích hình nón cụt
    r1: bán kính đáy lớn
    r2: bán kính đáy nhỏ
    height: chiều cao
    """
    return (math.pi * height / 3) * (r1**2 + r1*r2 + r2**2)

def sphere_surface_area(radius):
    """Diện tích mặt cầu"""
    return 4 * math.pi * radius**2

# Example usage
vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
area = polygon_area(vertices)
print(f"Diện tích đa giác: {area} đơn vị²")

volume = truncated_cone_volume(5, 3, 8)
print(f"Thể tích hình nón cụt: {volume:.2f} đơn vị³")
```

### Ma trận và Determinant

```python
def matrix_multiply(A, B):
    """
    Nhân hai ma trận
    A: ma trận m×n
    B: ma trận n×p
    Returns: ma trận m×p
    """
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    if cols_A != len(B):
        raise ValueError("Không thể nhân ma trận: kích thước không tương thích")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def determinant_2x2(matrix):
    """Tính determinant ma trận 2×2"""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    """Tính determinant ma trận 3×3"""
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    return (a * (e*i - f*h) -
            b * (d*i - f*g) +
            c * (d*h - e*g))

# Example
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
print(f"A × B = {result}")

matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
det = determinant_3x3(matrix_3x3)
print(f"Determinant 3×3: {det}")
```

### Chuỗi toán học

```python
import math

def taylor_sin(x, terms=10):
    """
    Tính sin(x) sử dụng Taylor series
    sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...
    """
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        numerator = x ** (2*n + 1)
        denominator = math.factorial(2*n + 1)
        result += sign * numerator / denominator
    return result

def taylor_cos(x, terms=10):
    """
    Tính cos(x) sử dụng Taylor series
    cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
    """
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        numerator = x ** (2*n)
        denominator = math.factorial(2*n)
        result += sign * numerator / denominator
    return result

def taylor_exp(x, terms=20):
    """
    Tính e^x sử dụng Taylor series
    e^x = 1 + x + x²/2! + x³/3! + ...
    """
    result = 0
    for n in range(terms):
        result += x**n / math.factorial(n)
    return result

# Compare with built-in functions
x = math.pi / 4
print(f"sin({x}) - Taylor: {taylor_sin(x):.6f}, Built-in: {math.sin(x):.6f}")
print(f"cos({x}) - Taylor: {taylor_cos(x):.6f}, Built-in: {math.cos(x):.6f}")
print(f"exp({x}) - Taylor: {taylor_exp(x):.6f}, Built-in: {math.exp(x):.6f}")
```

## Module 2: Tính toán khoa học

### Áp suất khí lý tưởng

```python
def ideal_gas_law(P=None, V=None, n=None, R=8.314, T=None):
    """
    Phương trình khí lý tưởng: PV = nRT
    P: áp suất (Pa)
    V: thể tích (m³)
    n: số mol
    R: hằng số khí (J/mol·K)
    T: nhiệt độ (K)
    """
    # Count None values
    none_count = sum(x is None for x in [P, V, n, T])

    if none_count != 1:
        raise ValueError("Cần cung cấp chính xác 3 trong 4 giá trị")

    if P is None:
        return n * R * T / V
    elif V is None:
        return n * R * T / P
    elif n is None:
        return P * V / (R * T)
    elif T is None:
        return P * V / (n * R)

# Example: Tính áp suất
pressure = ideal_gas_law(V=10, n=1, T=300)
print(f"Áp suất: {pressure:.2f} Pa")

# Verification
verification = (pressure * 10) / (1 * 8.314 * 300)
print(f"Verification PV/nRT = {verification:.3f} ≈ 1")
```

### Năng lượng cơ học

```python
def kinetic_energy(mass, velocity):
    """Tính động năng: KE = ½mv²"""
    return 0.5 * mass * velocity**2

def potential_energy(mass, height, g=9.81):
    """Tính thế năng: PE = mgh"""
    return mass * g * height

def total_mechanical_energy(mass, velocity, height, g=9.81):
    """Tổng cơ năng"""
    ke = kinetic_energy(mass, velocity)
    pe = potential_energy(mass, height, g)
    return ke + pe

# Conservation of energy
def velocity_at_height(initial_velocity, initial_height, final_height, g=9.81):
    """Tính vận tốc tại độ cao khác (bảo toàn năng lượng)"""
    delta_pe = g * (final_height - initial_height)
    final_velocity_squared = initial_velocity**2 - 2 * delta_pe

    if final_velocity_squared < 0:
        return 0  # Object doesn't reach that height

    return math.sqrt(final_velocity_squared)

# Example
mass = 10  # kg
initial_v = 20  # m/s
height = 5  # m

ke = kinetic_energy(mass, initial_v)
pe = potential_energy(mass, height)

print(f"Động năng: {ke} J")
print(f"Thế năng: {pe} J")
print(f"Tổng cơ năng: {ke + pe} J")
```

### Sóng và dao động

```python
def wave_properties(frequency=None, wavelength=None, speed=None):
    """
    Tính toán tính chất sóng
    v = f × λ (speed = frequency × wavelength)
    """
    none_count = sum(x is None for x in [frequency, wavelength, speed])

    if none_count != 1:
        raise ValueError("Cần cung cấp chính xác 2 trong 3 giá trị")

    if frequency is None:
        return speed / wavelength
    elif wavelength is None:
        return speed / frequency
    elif speed is None:
        return frequency * wavelength

def doppler_effect(source_freq, source_velocity, observer_velocity, sound_speed=343):
    """
    Hiệu ứng Doppler
    f' = f × (v + v_observer) / (v + v_source)
    """
    observed_freq = source_freq * (sound_speed + observer_velocity) / (sound_speed + source_velocity)
    return observed_freq

# Example
freq = 440  # Hz (note A4)
speed = 343  # m/s (sound speed in air)
wavelength = wave_properties(frequency=freq, speed=speed)

print(f"Tần số: {freq} Hz")
print(f"Bước sóng: {wavelength:.3f} m")
print(f"Tốc độ: {speed} m/s")

# Doppler effect
doppler_freq = doppler_effect(440, -10, 0)  # Source moving away
print(f"Tần số Doppler: {doppler_freq:.1f} Hz")
```

## Module 3: Toán học tài chính

### Lãi suất kép

```python
def compound_interest(principal, rate, time, compounding_frequency=1):
    """
    Tính lãi suất kép
    A = P(1 + r/n)^(nt)
    """
    amount = principal * (1 + rate/compounding_frequency)**(compounding_frequency * time)
    interest = amount - principal
    return amount, interest

def continuous_compounding(principal, rate, time):
    """Lãi suất kép liên tục: A = Pe^(rt)"""
    amount = principal * math.exp(rate * time)
    return amount

def effective_annual_rate(nominal_rate, compounding_frequency):
    """Tính lãi suất hiệu dụng hàng năm"""
    return (1 + nominal_rate/compounding_frequency)**compounding_frequency - 1

# Example
principal = 10000  # $10,000
rate = 0.08  # 8% annual rate
time = 10  # years

# Different compounding frequencies
frequencies = [1, 4, 12, 365]  # Annual, Quarterly, Monthly, Daily
names = ["Annual", "Quarterly", "Monthly", "Daily"]

print("Compound Interest Analysis:")
for freq, name in zip(frequencies, names):
    amount, interest = compound_interest(principal, rate, time, freq)
    print(f"{name:10}: ${amount:,.2f} (Interest: ${interest:,.2f})")

# Continuous compounding
continuous_amount = continuous_compounding(principal, rate, time)
print(f"Continuous: ${continuous_amount:,.2f}")
```

### Loan Amortization

```python
def monthly_payment(principal, annual_rate, years):
    """Tính payment hàng tháng cho loan"""
    monthly_rate = annual_rate / 12
    num_payments = years * 12

    if monthly_rate == 0:
        return principal / num_payments

    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
              ((1 + monthly_rate)**num_payments - 1)
    return payment

def amortization_schedule(principal, annual_rate, years, num_payments_to_show=12):
    """Tạo lịch trả nợ"""
    monthly_rate = annual_rate / 12
    payment = monthly_payment(principal, annual_rate, years)

    balance = principal
    schedule = []

    for month in range(min(num_payments_to_show, years * 12)):
        interest_payment = balance * monthly_rate
        principal_payment = payment - interest_payment
        balance -= principal_payment

        schedule.append({
            'month': month + 1,
            'payment': payment,
            'principal': principal_payment,
            'interest': interest_payment,
            'balance': balance
        })

    return schedule

# Example
loan_amount = 200000  # $200,000 home loan
annual_rate = 0.05  # 5% interest
years = 30

payment = monthly_payment(loan_amount, annual_rate, years)
print(f"Monthly payment: ${payment:.2f}")

schedule = amortization_schedule(loan_amount, annual_rate, years, 6)
print("\nAmortization Schedule (first 6 months):")
print("Month | Payment  | Principal | Interest | Balance")
print("-" * 50)
for row in schedule:
    print(f"{row['month']:5} | ${row['payment']:7.2f} | ${row['principal']:8.2f} | "
          f"${row['interest']:7.2f} | ${row['balance']:,.2f}")
```

### Portfolio Analysis

```python
def portfolio_return(weights, returns):
    """Tính portfolio return"""
    return sum(w * r for w, r in zip(weights, returns))

def portfolio_variance(weights, covariance_matrix):
    """Tính portfolio variance"""
    n = len(weights)
    variance = 0

    for i in range(n):
        for j in range(n):
            variance += weights[i] * weights[j] * covariance_matrix[i][j]

    return variance

def sharpe_ratio(portfolio_return, risk_free_rate, portfolio_std):
    """Tính Sharpe ratio"""
    return (portfolio_return - risk_free_rate) / portfolio_std

# Example portfolio
assets = ['Stock A', 'Stock B', 'Bond C']
weights = [0.4, 0.4, 0.2]
expected_returns = [0.12, 0.15, 0.05]  # 12%, 15%, 5%

# Covariance matrix (simplified)
cov_matrix = [
    [0.04, 0.02, 0.01],
    [0.02, 0.06, 0.015],
    [0.01, 0.015, 0.02]
]

port_return = portfolio_return(weights, expected_returns)
port_variance = portfolio_variance(weights, cov_matrix)
port_std = math.sqrt(port_variance)

print(f"Portfolio Return: {port_return:.1%}")
print(f"Portfolio Risk (σ): {port_std:.1%}")

risk_free = 0.03  # 3% risk-free rate
sharpe = sharpe_ratio(port_return, risk_free, port_std)
print(f"Sharpe Ratio: {sharpe:.2f}")
```

## Module 4: Statistics và Probability

### Descriptive Statistics

```python
def mean(data):
    """Tính trung bình"""
    return sum(data) / len(data)

def median(data):
    """Tính trung vị"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def mode(data):
    """Tìm mode (giá trị xuất hiện nhiều nhất)"""
    from collections import Counter
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

def standard_deviation(data):
    """Tính độ lệch chuẩn"""
    avg = mean(data)
    variance = sum((x - avg)**2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)

def quartiles(data):
    """Tính quartiles Q1, Q2, Q3"""
    sorted_data = sorted(data)
    n = len(sorted_data)

    q2 = median(sorted_data)
    q1 = median(sorted_data[:n//2])
    q3 = median(sorted_data[(n+1)//2:])

    return q1, q2, q3

# Example
dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4]

print(f"Mean: {mean(dataset):.2f}")
print(f"Median: {median(dataset):.2f}")
print(f"Mode: {mode(dataset)}")
print(f"Standard Deviation: {standard_deviation(dataset):.2f}")

q1, q2, q3 = quartiles(dataset)
print(f"Quartiles: Q1={q1}, Q2={q2}, Q3={q3}")
```

### Linear Regression

```python
def linear_regression(x_data, y_data):
    """
    Tính linear regression: y = mx + b
    Returns: slope (m), intercept (b), correlation coefficient (r)
    """
    n = len(x_data)
    sum_x = sum(x_data)
    sum_y = sum(y_data)
    sum_xy = sum(x * y for x, y in zip(x_data, y_data))
    sum_x2 = sum(x**2 for x in x_data)
    sum_y2 = sum(y**2 for y in y_data)

    # Calculate slope and intercept
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n

    # Calculate correlation coefficient
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
    correlation = numerator / denominator if denominator != 0 else 0

    return slope, intercept, correlation

def predict(x, slope, intercept):
    """Dự đoán y từ x sử dụng linear model"""
    return slope * x + intercept

# Example data
x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_data = [2.1, 3.9, 6.1, 8.0, 9.9, 12.1, 14.0, 16.1, 18.0, 19.9]

slope, intercept, correlation = linear_regression(x_data, y_data)

print(f"Linear Regression: y = {slope:.3f}x + {intercept:.3f}")
print(f"Correlation coefficient: {correlation:.3f}")

# Prediction
x_new = 11
y_pred = predict(x_new, slope, intercept)
print(f"Prediction for x={x_new}: y={y_pred:.2f}")
```

### Monte Carlo Simulation

```python
import random

def monte_carlo_pi(num_simulations):
    """Ước tính π sử dụng Monte Carlo method"""
    inside_circle = 0

    for _ in range(num_simulations):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_simulations
    return pi_estimate

def monte_carlo_integration(func, a, b, num_simulations):
    """Tích phân Monte Carlo"""
    total = 0

    for _ in range(num_simulations):
        x = random.uniform(a, b)
        total += func(x)

    integral = (b - a) * total / num_simulations
    return integral

# Example: Estimate π
simulations = 1000000
pi_estimate = monte_carlo_pi(simulations)
print(f"π estimate with {simulations} simulations: {pi_estimate:.4f}")
print(f"Actual π: {math.pi:.4f}")
print(f"Error: {abs(pi_estimate - math.pi):.4f}")

# Example: Integrate x² from 0 to 1
def square_function(x):
    return x**2

integral = monte_carlo_integration(square_function, 0, 1, 100000)
print(f"∫₀¹ x² dx ≈ {integral:.4f} (Exact: 0.3333)")
```

## Module 5: Engineering Calculations

### Circuit Analysis

```python
def ohms_law(voltage=None, current=None, resistance=None):
    """
    Ohm's Law: V = I × R
    Provide 2 values, get the third
    """
    none_count = sum(x is None for x in [voltage, current, resistance])

    if none_count != 1:
        raise ValueError("Provide exactly 2 values")

    if voltage is None:
        return current * resistance
    elif current is None:
        return voltage / resistance
    elif resistance is None:
        return voltage / current

def power_calculations(voltage=None, current=None, resistance=None, power=None):
    """
    Power calculations: P = VI = I²R = V²/R
    """
    none_count = sum(x is None for x in [voltage, current, resistance, power])

    if none_count != 2:
        raise ValueError("Provide exactly 2 values")

    # If we have V and I
    if voltage is not None and current is not None:
        return {
            'power': voltage * current,
            'resistance': voltage / current
        }

    # If we have V and R
    if voltage is not None and resistance is not None:
        return {
            'current': voltage / resistance,
            'power': voltage**2 / resistance
        }

    # Add more combinations as needed...

def parallel_resistance(*resistances):
    """Tính điện trở tương đương mạch song song"""
    return 1 / sum(1/r for r in resistances)

def series_resistance(*resistances):
    """Tính điện trở tương đương mạch nối tiếp"""
    return sum(resistances)

# Example
voltage = 12  # V
resistance = 100  # Ω

current = ohms_law(voltage=voltage, resistance=resistance)
power = voltage * current

print(f"Circuit Analysis:")
print(f"Voltage: {voltage} V")
print(f"Resistance: {resistance} Ω")
print(f"Current: {current:.3f} A")
print(f"Power: {power:.3f} W")

# Parallel resistors
r_parallel = parallel_resistance(100, 200, 300)
print(f"Parallel resistance (100Ω || 200Ω || 300Ω): {r_parallel:.1f}Ω")
```

### Heat Transfer

```python
def conduction_heat_transfer(k, area, temp_diff, thickness):
    """
    Heat transfer by conduction: Q = kA(ΔT)/d
    k: thermal conductivity
    area: cross-sectional area
    temp_diff: temperature difference
    thickness: material thickness
    """
    return k * area * temp_diff / thickness

def convection_heat_transfer(h, area, temp_diff):
    """
    Heat transfer by convection: Q = hA(ΔT)
    h: convection coefficient
    """
    return h * area * temp_diff

def radiation_heat_transfer(emissivity, area, temp_hot, temp_cold, stefan_boltzmann=5.67e-8):
    """
    Heat transfer by radiation: Q = εσA(T₁⁴ - T₂⁴)
    Temperatures in Kelvin
    """
    return emissivity * stefan_boltzmann * area * (temp_hot**4 - temp_cold**4)

# Example
k_aluminum = 237  # W/m·K
area = 0.01  # m²
temp_diff = 50  # K
thickness = 0.005  # m

q_conduction = conduction_heat_transfer(k_aluminum, area, temp_diff, thickness)
print(f"Heat transfer by conduction: {q_conduction:.1f} W")

# Convection
h_air = 25  # W/m²·K
q_convection = convection_heat_transfer(h_air, area, temp_diff)
print(f"Heat transfer by convection: {q_convection:.1f} W")
```

## Performance Optimization và Best Practices

### Numerical Precision

```python
import decimal

def high_precision_calculation():
    """Sử dụng decimal cho precision cao"""
    decimal.getcontext().prec = 50

    a = decimal.Decimal('1') / decimal.Decimal('3')
    b = a * 3

    print(f"High precision: 1/3 × 3 = {b}")

    # So sánh với float
    a_float = 1/3
    b_float = a_float * 3
    print(f"Float precision: 1/3 × 3 = {b_float}")

def avoid_floating_point_errors():
    """Cách tránh lỗi floating point"""
    # Wrong way
    if 0.1 + 0.2 == 0.3:
        print("Equal")
    else:
        print("Not equal!")  # This will print

    # Right way
    epsilon = 1e-10
    if abs((0.1 + 0.2) - 0.3) < epsilon:
        print("Equal (within tolerance)")

high_precision_calculation()
avoid_floating_point_errors()
```

### Error Handling

```python
def safe_calculation(func, *args, **kwargs):
    """Wrapper để handle mathematical errors"""
    try:
        result = func(*args, **kwargs)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except ValueError as e:
        print(f"Value error: {e}")
        return None
    except OverflowError:
        print("Error: Numerical overflow")
        return None

def validate_input(value, min_val=None, max_val=None, name="Value"):
    """Validate numerical input"""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")

    if min_val is not None and value < min_val:
        raise ValueError(f"{name} must be >= {min_val}")

    if max_val is not None and value > max_val:
        raise ValueError(f"{name} must be <= {max_val}")

    return True

# Example usage
try:
    validate_input(-5, min_val=0, name="Interest rate")
except ValueError as e:
    print(f"Validation error: {e}")
```

## Tips để thành công

### 1. Organization và Modularity

```python
class FinancialCalculator:
    """Tổ chức code thành classes cho reusability"""

    @staticmethod
    def compound_interest(principal, rate, time, frequency=1):
        return principal * (1 + rate/frequency)**(frequency * time)

    @staticmethod
    def present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
```

### 2. Documentation và Testing

```python
def quadratic_solver(a, b, c):
    """
    Solve quadratic equation ax² + bx + c = 0

    Args:
        a (float): coefficient of x²
        b (float): coefficient of x
        c (float): constant term

    Returns:
        tuple: (x1, x2, discriminant) or None if no real solutions

    Examples:
        >>> quadratic_solver(1, -5, 6)
        (3.0, 2.0, 1.0)
    """
    # Implementation here
    pass

# Unit tests
def test_quadratic_solver():
    result = quadratic_solver(1, -5, 6)
    assert abs(result[0] - 3.0) < 1e-10
    assert abs(result[1] - 2.0) < 1e-10
```

### 3. Performance Monitoring

```python
import time
import functools

def timing_decorator(func):
    """Decorator để measure execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def expensive_calculation():
    # Complex calculation here
    pass
```

Hãy thực hành implement các calculations một cách cẩn thận, chú ý đến precision và error handling!

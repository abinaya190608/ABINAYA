def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.
    
    Parameters:
    principal (float): The principal amount
    rate (float): The annual interest rate (in %)
    time (float): The time in years
    
    Returns:
    float: The calculated simple interest
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage
if __name__ == "__main__":
    P = float(input("Enter the principal amount: "))
    R = float(input("Enter the annual rate of interest (in %): "))
    T = float(input("Enter the time (in years): "))

    SI = calculate_simple_interest(P, R, T)
    print(f"Simple Interest = {SI:.2f}")

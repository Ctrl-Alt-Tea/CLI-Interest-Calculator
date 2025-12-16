def calculate_simple_interest(principal, annual_rate, years, monthly_contribution=0):
    total_contributions = monthly_contribution * 12 * years
    total_principal = principal + total_contributions
    interest = total_principal * annual_rate * years
    final_value = total_principal + interest
    return interest, final_value

def calculate_compound_interest(principal, annual_rate, years, monthly_contribution=0):
    months = years * 12
    monthly_rate = annual_rate / 12
    future_value = principal * (1 + monthly_rate) ** months
    for month in range(1, months + 1):
        future_value += monthly_contribution * (1 + monthly_rate) ** (months - month)
    interest = future_value - (principal + monthly_contribution * months)
    return interest, future_value

def main():
    print("Interest Calculator")
    print("")
    interest_type = input("Choose interest type (simple [1] or compound [2]): ").strip().lower()
    principal = float(input("Enter initial deposit amount: R"))
    annual_rate = float(input("Enter annual interest rate (e.g., 6.5 for 6.5%): ")) / 100
    years = int(input("Enter investment duration in years: "))
    monthly_contribution = float(input("Enter monthly contribution amount (R0 if none): R"))

    if interest_type == "1":
        interest, final_value = calculate_simple_interest(principal, annual_rate, years, monthly_contribution)
    elif interest_type == "2":
        interest, final_value = calculate_compound_interest(principal, annual_rate, years, monthly_contribution)
    else:
        print("Invalid interest type selected.")
        return


    print("")
    print(f"\nResults after {years} years:")
    print(f"Total Interest Earned: R{interest:.2f}")
    print(f"Final Value of Investment: R{final_value:.2f}")
    print(" ")

if __name__ == "__main__":
    main()

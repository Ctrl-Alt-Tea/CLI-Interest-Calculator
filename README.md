# 💸 pyZAR Interest Calculator

A simple Python script that helps users calculate **simple** or **compound interest** on their investments. It also supports **monthly contributions**, making it useful for savings planning and financial forecasting.

## 📦 Features

- Choose between **Simple** or **Compound** interest
- Input:
  - Initial deposit amount
  - Annual interest rate
  - Investment duration (in years)
  - Optional monthly contributions
- Outputs:
  - Total interest earned
  - Final value of the investment

## 🧮 How It Works
  ```
  Interest = (Principal + Contributions) × Rate × Time
  Future Value = Principal × (1 + Monthly Rate)^(Months)
  Compound Interest is calculated monthly
  ```

## 🚀 Getting Started

### Requirements
- Python 3.x

### Run the Script in your terminal
```bash
python interest_calculator.py
```

## Examle Usage
### Input
```
Choose interest type (simple/compound): compound
Enter initial deposit amount: R20000
Enter annual interest rate (e.g., 6.5 for 6.5%): 6.5
Enter investment duration in years: 5
Enter monthly contribution amount (R0 if none): R0
```
### Output
```
Results after 5 years:
Total Interest Earned: R7656.35
Final Value of Investment: R27656.35
```

## 🛠️ Future Improvements
- Add a GUI using Tkinter or WPF
- Export results to CSV or PDF
- Add support for different compounding frequencies (quarterly, daily)

## Contact
Feel free to drop any suggestions or bug reports (dylanrose.sa@gmail.com)

### Support the project:
<a href="https://www.zapper.com/payWithZapper/?qr=http%3A%2F%2F2.zap.pe%3Ft%3D6%26i%3D64641%3A82254%3A7%5B34%7C0%2C33n%7CWebsite%20Donation%7C11%7CReference%3A10%5B39%7CZAR%2C38%7CDylans%20Store" target="_blank"><img src="https://www.zapper.com/wp-content/uploads/2023/08/Zapper-Logo.png" alt="Donate Via Zapper" style="height: 60px !important;width: 217px !important;" ></a>

<a href="https://www.buymeacoffee.com/dylanrose" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

# Function to give health tips based on BMI
def give_health_tip(bmi):
    if bmi < 18.5:
        return "You're underweight. Consider increasing calorie intake with nutritious food."
    elif bmi < 24.9:
        return "You're in the normal range. Keep up the good work with a balanced diet!"
    elif bmi < 29.9:
        return "You're overweight. Try to increase physical activity and monitor your diet."
    else:
        return "You're in the obese range. Consult a healthcare professional for guidance."

# Function to plot BMI categories and user's BMI
def plot_bmi(bmi):
    categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
    bmi_ranges = [18.5, 24.9, 29.9, 40]
    colors = ['#AEC6CF', '#77DD77', '#FFB347', '#FF6961']  # Blue, Green, Orange, Red
    
    plt.figure(figsize=(10, 6))
    
    # Plot BMI categories
    plt.bar(categories, bmi_ranges, color=colors, edgecolor='black')
    
    # Mark user's BMI
    plt.axhline(y=bmi, color='blue', linestyle='--', label=f'Your BMI: {bmi:.2f}')
    
    # Mark average BMI
    avg_bmi = 23
    plt.axhline(y=avg_bmi, color='green', linestyle=':', label=f'Avg BMI: {avg_bmi}')
    
    # Add BMI values on top of bars
    for i, value in enumerate(bmi_ranges):
        plt.text(i, value - 3, f'{value:.1f}', ha='center', color='black', fontsize=10)
    
    plt.title('BMI Categories', fontsize=16)
    plt.ylabel('BMI Value', fontsize=12)
    plt.legend()
    
    # Save the plot as an image
    plt.savefig('bmi_chart.png')
    print("BMI chart saved as 'bmi_chart.png'")
    
    plt.show()

# Main function
def main():
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in cm): "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return
        
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
        
        # Display health tip
        tip = give_health_tip(bmi)
        print(f"Health Tip: {tip}")
        
        # Plot BMI categories and user's BMI
        plot_bmi(bmi)
    
    except ValueError:
        print("Please enter valid numbers for weight and height.")

# Run the code only if executed directly
if __name__ == "__main__":
    main()

# know-you-pet-vaccination-dates


# Dog Vaccination Guide Tool 🐾

A Python command-line application that helps pet owners determine the correct vaccination schedule for their dogs and puppies. The tool interacts with the user, collects details about the dog's age and breed type, applies conditional logic to provide specific veterinary recommendations, and generates a personalized **Digital Vaccination Card**.

## 🚀 Features
* **Interactive CLI:** Greets users with custom ASCII dog art and guides them through step-by-step prompts.
* **Smart Recommendations:** Uses nested conditional logic to separate puppy care (weeks) from adult dog care (months).
* **Dynamic Summaries:** Outputs a clean, formatted Vaccination Card detailing the dog's name, age, breed, owner, and scheduled date.

## 🛠️ Tech Stack & Concepts Used
* **Language:** Python 3
* **Control Flow:** `if`, `elif`, and `else` statements for decision-making.
* **Logical Operations:** Conditional branching based on user inputs.
* **String Manipulation:** Multi-line strings for ASCII art and `f-strings` for dynamic data printing.
* **Data Input Handling:** Capturing text and numeric inputs seamlessly from the terminal.

## 📋 How It Works
1. Run the script in your terminal.
2. Enter your pet's name and confirm if you want to proceed.
3. Select whether your dog is a **puppy** or an **adult dog**.
4. Provide their current age to receive tailored vaccination milestones.
5. Input the appointment date and owner details to generate the final receipt card.

## 📝 Example Output
```text
------VACCINATION CARD------
Dog name: Buddy
Age: 6 months/weeks
Breed: puppy
Vaccination date: 15/06/2026
Owner of dog/puppy: Alex
******Thank you******
```

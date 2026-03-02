import time

def get_human_factors_from_user():
    print("\nEnter psychological factors as percentages (0-100):\n")
    try:
        emotion = float(input("Emotion (%): ")) / 100
        memory = float(input("Memory (%): ")) / 100
        social_pressure = float(input("Social Pressure (%): ")) / 100
        risk_tolerance = float(input("Risk Tolerance (%): ")) / 100
    except ValueError:
        print("Invalid input! Using default 50% for all factors.")
        emotion = memory = social_pressure = risk_tolerance = 0.5

    return {
        "emotion": emotion,
        "memory": memory,
        "social_pressure": social_pressure,
        "risk_tolerance": risk_tolerance
    }

def calculate_decision_probability(factors):
    weight_emotion = 0.35
    weight_memory = 0.25
    weight_social = 0.20
    weight_risk = 0.20

    probability = (
        factors["emotion"] * weight_emotion +
        factors["memory"] * weight_memory +
        factors["social_pressure"] * weight_social +
        factors["risk_tolerance"] * weight_risk
    )

    return probability


def predict_decision():
    print("\nWelcome to the cognitive prediction model.\n")
    
    option1 = input("Enter first choice: ")
    option2 = input("Enter second choice: ")

    factors = get_human_factors_from_user()

    print("\nAnalyzing behavioral outcome...\n")
    time.sleep(1.2)

    for key, value in factors.items():
        print(f"{key.capitalize():<18}: {value:.2f}")
        time.sleep(0.4)

    probability = calculate_decision_probability(factors)

    predicted_choice = option1 if probability >= 0.5 else option2
    confidence = abs(probability - 0.5) * 2

    print("\n--- Prediction Result ---")
    print(f"Predicted Choice : {predicted_choice}")
    print(f"Decision Bias    : {probability * 100:.1f}%")
    print(f"Confidence Level : {confidence * 100:.1f}%")

    print("\nModel Interpretation:")
    print("Human decision influenced by weighted psychological signals.")

if __name__ == "__main__":
    predict_decision()
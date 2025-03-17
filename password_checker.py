# List that holds feedback messages.
feedback = []
# Variable that keeps track of the score.
score = 0


# Main function that starts the password strength testing process.
def main():
    print("Welcome to Password Strength Tester!\n")
    
    # Prompt the user to enter a password.
    password = input("Enter password: ").strip()
    strengthTest(password) # Calls strengthTest function to evaluate the password.

    # Print user feedback.
    print("\nPassword Feedback:\n")
    # Loop through the feedback list and print each feedback message.
    for i in feedback:
        print(i)
    
    # Print the total score out of 14 and the percentage score.
    print(f"\n{score}/14. You get a {round((score/14) * 100, 2)}%!")


# Function to evaluate the overall strength of the password.
def strengthTest(password):
    global score # Access and modify the global score variable.

    # Call each function and accumulate the score based on their results.
    score += lengthTest(password) # Evaluate the password length.
    score += letterTest(password) # Evaluate the number and types of characters in the password.
    score += digitTest(password) # Evaluate the number of digits in the password.
    score += punctuationTest(password) # Evaluate the number of punctuation characters in the password.


# Function to check the length of the password and assign a score.
def lengthTest(password):
    # Check if the password is too short (8 characters or fewer).
    if len(password) <= 8:
        # Provide feedback and assign +1 point.
        feedback.append("Password should be longer than 8 characters. +1") 
        return 1
    # Check if the password length is between 9 and 16 characters.
    elif 8 < len(password) <= 16:
        # Provide feedback and assign +2 points.
        feedback.append("Good length. However, you should aim for more than 16 characters for extra security measures. +2")
        return 2
    # If the password is longer than 16 characters.
    else:
        # Provide feedback and assign +3 point.
        feedback.append("Password has an optimal amount of characters. +3")
        return 3
    

# Function to evaluate the letter-related criteria of the password.
def letterTest(password):
    score = 0 # Initialize the score for this test. 

    # Check if the password has at least four alphabetic characters.
    if sum(1 for char in password if char.isalpha()) >= 4:
        # Provide feedback and assign +2 points.
        feedback.append("Password has more than four alphabetic characters. +2")
        score += 2 
    else:
        # Provide feedback and assign +1 point.
        feedback.append("Password should have at least four alphabetic characters. +1")
        score += 1
    
    # Check if the password contains at least two uppercase characters.
    if sum(1 for s in password if s.isupper()) >= 2:
        # Provide feedback and assign +2 points.
        feedback.append("Password has at least two uppercase characters. +2")
        score += 2
    # If the password has exactly one uppercase letter
    elif sum(1 for s in password if s.isupper()) == 1:
        # Provide feedback for exactly one uppercase letter and assign +1 point.
        feedback.append("Password has at least one uppercase character. +1")
        score += 1
    else:
        # Provide feedback and assign no points.
        feedback.append("Password has no uppercase characters. +0")
        score += 0 

    # Check if the password contains at least two lowercase characters.
    if sum(1 for s in password if s.islower()) >= 2:
        # Provide feedback and assign +2 points.
        feedback.append("Password has at least two lowercase characters. +2")
        score += 2
    # If the password has exactly one lowercase letter.
    elif sum(1 for s in password if s.islower()) >= 1:
        # Provide feedback and assign +1 point.
        feedback.append("Password has at least one lowercase letter. +1")
        score += 1
    else:
        feedback.append("Password has no lowercase characters. +0")
        score += 0
    
    # Return the total score from the letter tests.
    return score


# Function to check the number of digits in the password.
def digitTest(password):
    # Check if there are four or more digits in the password.
    if sum(c.isdigit() for c in password) >= 4:
        # Provide feedback and assign +2 points.
        feedback.append("Password has at least four digits. +2")
        return 2
    # Check if the password has between 1 and 3 digits.
    elif 1 <= sum(c.isdigit() for c in password) < 4:
        # Provide feedback and assign +1 point.
        feedback.append("Password has between one and three digits. +1")
        return 1
    else:
        # Provide feedback and assign no points.
        feedback.append("Password has no digits. +0")
        return 0


# Function to check the number of punctuation characters in the password.
def punctuationTest(password):
    # List that holds all punctuation characters.
    punctuation =  [
        "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", 
        ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", 
        "}", "~"
    ]

    # Check if there are 3 or more punctuation characters in the password
    if sum(1 for c in password if c in punctuation) >= 3:
        # Provide feedback and assign +3 points
        feedback.append("Password has at least three punctuation characters. +3")
        return 3
    # Check if the password has between 1 and 2 punctuation characters
    elif 1 <= sum(1 for c in password if c in punctuation) < 3:
        # Provide feedback and assign +1 point.
        feedback.append("Password has at least one punctuation character. +1")
        return 1
    else:
        # Provide feedback and assign no points.
        feedback.append("Password has no punctuation characters. +0")
        return 0


# Main code entry point.
if __name__ == "__main__":
    main() # Call the main function to run the password strength checker.

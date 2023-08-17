import cv2
from keras.models import load_model
import numpy as np
import random
import time

def load_labels(file_path):
    with open(file_path, 'r') as file:
        labels = {}
        for line in file:
            label_id, label_name = line.strip().split(' ', 1)
            labels[int(label_id)] = label_name
    return labels

prediction_labels = load_labels('converted_keras/labels.txt')
game_results = {"Computer": 0, "User": 0}


def get_prediction(frame):
    model = load_model('converted_keras/keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    predicted_index = np.argmax(prediction)  # Get the index of the maximum prediction value
    predicted_label = prediction_labels.get(predicted_index, "Unknown")
    return predicted_label
 
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices).capitalize()
    return computer_choice

def get_winner(computer_choice, user_choice, dictionary):
    if computer_choice == user_choice:
        dictionary["Computer"] += 0
        dictionary["User"] += 0
    elif computer_choice == "Rock" and user_choice == "Paper":
        dictionary["User"] += 1
    elif computer_choice == "Rock" and user_choice == "Scissors":
        dictionary["Computer"] += 1
    elif computer_choice == "Paper" and user_choice == "Rock":
        dictionary["Computer"] += 1
    elif computer_choice == "Paper" and user_choice == "Scissors":
        dictionary["User"] += 1
    elif computer_choice == "Scissors" and user_choice == "Rock":
        dictionary["User"] += 1
    elif computer_choice == "Scissors" and user_choice == "Paper":
        dictionary["Computer"] += 1
    return dictionary


def play_game(dictionary):
    while dictionary["Computer"] < 3 and dictionary["User"] < 3:
        computer_choice = get_computer_choice()
        user_choice = None
        count_down()
        time.sleep(1)  # Give a little delay after the countdown
        ret, frame = cap.read()  # Capture a frame after the countdown

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        user_choice = get_prediction(frame)
        print(f"Computer picked {computer_choice}")
        print(f"You picked {user_choice}")
        print(get_winner(computer_choice, user_choice, dictionary))
    if dictionary["Computer"] == 3:
        print("Computer wins!")
        exit()
    elif dictionary["User"] == 3:
        print("You win!")
        exit()


def count_down():
    start_time = time.time()
    end_time = start_time + 3
    count_down = ["Rock", "Paper", "Scissors"]
    while time.time() < end_time:
        print(count_down[int(time.time() - start_time)])
        time.sleep(1)
    print("Shoot!")

cap = cv2.VideoCapture(0)

# Wait for user input before starting the game
input("Press Enter when you're ready to start the game...")

# Close the camera window opened during input
cv2.destroyAllWindows()

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    play_game(game_results)  # Pass 'cap' as an argument

# Release the camera after the game is played
cap.release()
cv2.destroyAllWindows()

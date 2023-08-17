# Computer Vision RPS
Leveraging Teachable Machine, I have trained and developed a model, with 4 different classes. 
3 classes represent the three options of Rock, Paper, Scissors, and the fourth class represents none of them.
An average of 22 images were used to train each class. Teachable Machine allows us to test the accuracy of the
model live on their website, and I have noticed that there is a slight innacuracy in the model, nonetheless,
I am going to continue with the development of the code with the model as is out of curiousty. At the end if I realize 
this is being an issue I will upload more photos to the model and update it. 

The model was exported using keras and added to the folder containing the code/repository.

Following this I had to set up the virtual environment for the project. A step that is usually, straightforward proved to be more difficult due to complications
of using an M1 Apple. Initially, none of the packages, were installing, tensorflow created many issues. I connected with the support team, and we discussed that it
could be an issue with anaconda. So after some research the support team recommended trying miniforge instead of anaconda. This solved the issue of installing the 
tensorflow packages, however, an error kept occuring with the opencv package. Nonetheless, this confirmed that the issue was with anaconda. So I decided to uninstall 
anaconda from my computer. Before completing this step I had to backup all of my code which I use for my job as a data analyst as they were all anaconda linked and there was 
a chance they would be deleted. Once that was completed creating the virtual environment and downloading the required packages was fairly straightforward. 
For reference this was very helpful in solving the issue: https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706. 

Once that was done, I was able to run RPS-Template, and see how it works, and saw that it was infact returning an array which represented the prediction the model was giving. 

I then moved onto the next task (manual_rps) which was to build a straight forward game of rock,paper,scissors between the computer and the user. The code has 4 functions, one 
which asks the user to input either rock, paper or scissors. Although the task didnt directly include building catch and error message for the user input, I decided to incorporate that in my 
code. The next function build was to get the computers randomly generated response from the possible three choices of rock,paper,scissors. The third function, would take the 
output generated from the two previous functions, and decide on a winner. The final function, takes in all the previous functions and stimulates a game.

The next task was to write a new python script, camera_rps, which would use the webcam to take a picture of the user's hand as input instead of writting their input, and then use the model to predict what the user's hand gesture is. this essentially required 6 functions. T

he first function named load_labels, opened the labels.txt file from the model and loads what each prediction index refers to {0:Rock, 1:Paper, 2:Scissors, 3:None}. 
The second function is get_prediction, which takes in the image from the webcam, and uses the model to predict what the image is. 

The third function is get_computer_choice which essentially leverages the random library to randomly select either Rock,Paper or Scissors. 

The fourth function is get_winner, which takes in the user's choice and the computer's choice and decides who the winner is. Furthermore, it updates the score from the original dictionary game_results which is initialized at 0,0 and updates it based on the winner. 

The fifth function is the count_down function which essentially prints a countdown of Rock Paper Scissors,Shoot,in the terminal to give the user time to get their hand in position.


The final function is play game, which takes in all the previous functions and stimulates a game of rock,paper,scissors between the user and the computer. 

To have the entire code run in a loop, I created a while loop which would run the play_game function until there is a winner or the user decides to quit using the Q key. Furthermore, The game would commence once the user presses the Enter key.

General Comments: 
Although the model on Teachable_Machine is very accurate once that model is downloaded and used in Python its seems to loose some of its accuracy. I am not sure why this is the case, but I am assuming it has to do with the fact that the model is trained on a very small dataset. I am going to try to train the model on a larger dataset and see if that improves the accuracy.



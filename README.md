# QuickCare
QuickCare is a website designed to efficiently and reliably meet the basic healthcare needs of its users. 


## Inspiration

### Purpose
QuickCare, a website application designed to efficiently and reliably meet the basic
healthcare needs of its users, intends to solve many of the most pressing issues with the dern
healthcare system, including (but not limited to): a shortage of healthcare workers, limited access
to medical services among low-income individuals, and the delays associated with receiving
in-person medical attention. By providing easily accessible medical information to patients,
QuickCare expedites the treatment process and provides patients with the guidance to seek
further medical care when necessary.

### Relevance
As the volume of patients seeking medical attention and the overall demand for
convenient services increase, the need for automated healthcare reveals itself as one of the most
relevant issues of the modern age. This project team has concluded that a free, user-friendly
website application offering the most essential healthcare services and information would
achieve the greatest possible access to medical attention for individuals everywhere who require
it.

### Existing Solutions
In response to the widespread need for automated healthcare services, many solutions
have been deployed for patient use, such as platforms to communicate with doctors via online
video calls, websites to access treatment plans for various conditions, and questionnaires for
reporting symptoms and receiving medication prescriptions. However, each of these available
services either includes a fee or involves significant delays in the treatment process. For example, communicating with a doctor via video call requires a scheduled appointment, online
treatment plans are often costly, and medical questionnaires must be processed by human
physicians, which often takes up to an hour. In light of the drawbacks to existing solutions, this
project team developed a platform for providing convenient, fast, and cost-free
healthcare services to patients everywhere.

### Summary of Project Goal
This project team aimed to address the most pressing issues facing America's healthcare system and establish an efficient and inclusive way for patients to access affordable healthcare services. In order to do so, the team developed _QuickCare_, which is intended to **meet the basic medical and informational needs of its users, reduce the effects of economic disparity as it pertains to the American healthcare system, and serve as a building block toward quality healthcare accessible to all.**


## What It Does

_QuickCare_ is an application that uses a decision tree machine learning algorithm to offer effective medical advice and tips to patients. **It offers three main services: "Report Symptoms," "Emergency Instructions," and "General Wellness."**

### “Report Symptoms”
The **"Report Symptoms"** service allows users to input their symptoms via checkboxes. Hovering over each symptom in the form reveals a mini description, allowing patients to quickly and accurately assess whether or not they are experiencing the symptom in question. The application feeds this user input into a decision tree classification algorithm to provide an unofficial yet accurate diagnosis of the patient’s most likely condition. Moreover, it offers additional information about and treatment options for the identified condition. 

### “Emergency Instructions”
On the **"Emergency Instructions"** page, users can access information on how to handle common emergency situations with a search bar. For instance, when a user enters the search query “choking,” the application provides easy-to-follow instructions for dislodging the object obstructing the patient’s airflow and covers all basic protocols for interacting with the patient. All emergency directions and medical advice provided on the “Emergency Instructions” tab are recommended by reputable medical clinics such as Cleveland Clinic and Red Cross U.K. 

### “General Wellness”
On the **"General Wellness"** page, users can explore various health categories such as “Nutrition” and “Sleep” using clickable buttons that pull up information and medical advice pertaining to the given category. Clicking on a button shows an overview of the selected topic and guidelines for improving health in that area. 


## Challenges Encountered
Originally, the team planned to use A.I. to generate responses to search queries on _QuickCare_’s "Emergency Instructions" page using OpenAI’s API. However, in order to obviate the cost of frequent API calls, the team instead decided to incorporate a search bar function into the “Emergency Instructions” page that accesses a dictionary of several hard-coded emergency scenarios and outputs instructions according to the search query entered. 


## Accomplishments 
The team is particularly satisfied with the **decision tree classifier** machine learning model created to determine a patient’s condition based on their inputted symptoms. The model was trained on an extensive dataset of 4,920 training examples, each containing 132 potential symptoms and one of 41 potential conditions. Each training example consisted of 0s and 1s corresponding to each symptom (the features) along with a condition diagnosis (the label). 


## What Was Learned
Through this project, the team learned how to effectively address a real-world problem through the application of machine learning. Specifically, by training a model and deploying it for use within a website, this team was able to harness the predictive power of machine learning for use by anyone. In order to do this, team members learned to: develop a website using Python on the platform Anvil; design a user interface that is most appropriate for use by a wide variety of individuals; train, test, and evaluate various machine learning algorithms on Google Colaboratory using scikit-learn and pandas; deploy the chosen machine learning algorithm on the website using an uplink and a Docker container; and effectively locate errors and debug within a system of interacting parts, including the Colab notebook hosting the machine learning model, the frontend and backend servers of the website, and all files associated with the team’s Docker container. 


## Next Steps
In the future, this team aims to train the decision tree classification model on additional data so that it may output even more accurate predictions and account for a wider variety of possible symptoms. Furthermore, the team hopes to explore a broader range of machine learning techniques that may be useful for predicting a patient’s condition, such as the Naive Bayes and random forest algorithms as well as support vector machine models. Aside from this, the team hopes to collect feedback from those who interact with QuickCare via a short survey available on the website. This way, team members may change and add to the website so that it accounts for the needs and preferences of a wide range of users. 


# University Progression Prediction

A Python program to predict student progression outcomes based on their credit distribution in **Pass**, **Defer**, and **Fail** categories. This tool provides tailored functionalities for students and staff, including input validation, progression prediction, and histogram visualization for staff members.

## Features

- **Role Selection**: Choose between **Student** and **Staff** modes.
  - **Students**: Enter credit distribution to view progression outcome (one entry per session).
  - **Staff**: Input multiple students' credit data, view individual outcomes, and generate a histogram visualization of all progression outcomes.

- **Input Validation**: Ensures that credits entered are valid integers and within the specified ranges (multiples of 20, from 0 to 120).

- **Progression Prediction**: Based on the total credits in **Pass**, **Defer**, and **Fail**, the program predicts outcomes such as:
  - **Progress**
  - **Progress (Module Trailer)**
  - **Module Retriever**
  - **Exclude**

- **Histogram Visualization (for Staff Only)**: Displays a histogram of progression outcomes using `graphics.py`.

- **Data Storage (Optional)**: The program can store progression data in lists or save it to a text file for further analysis.

## Requirements

- **Python 3.x**
- **graphics.py** (for histogram visualization in staff mode)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Thiveya-Ratnarajah/university-progression-predictor.git

2. Navigate to the project directory:

   ```
   cd university-progression-prediction
  ** **Ensure you have Python 3.x installed.** **
## Usage

**Run the program:**

- python main.py
- **Student Mode**
Choose 1 when prompted to select your role.
Enter credits for Pass, Defer, and Fail.
The program will display your progression outcome and exit.

Example:


**Welcome! Please enter any one of the following values below to execute the program.**

    1. I am a student.
    2. I am a staff member.
    
Enter the number 1 or 2: 1


Enter your total PASS credits: 100

Enter your total DEFER credits: 20

Enter your total FAIL credits: 0


PROGRESSION OUTCOME: Progress (Module Trailer)

**Thank you! This program is successfully terminated.**

**---------------------------------------------------------------------------------------------------------------------------------**

- **Staff Mode**
Choose 2 when prompted to select your role.
Enter credits for each student:
Enter Pass, Defer, and Fail credits.
The program will display the Progression Outcome for each entry.
After each entry, you will be prompted to enter another student's data or quit to view the histogram.
Press Enter to continue adding data for additional students.
Press q to quit and view the histogram of progression outcomes.

Example:



**Welcome! Please enter any one of the following values below to execute the program.**

    1. I am a student. 
    2. I am a staff member.
    
Enter the number 1 or 2: 2

Enter your total PASS credits: 120

Enter your total DEFER credits: 0

Enter your total FAIL credits: 0


**PROGRESSION OUTCOME: Progress**


---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Would you like to enter another set of data?

Press 'Enter' key to continue or 'q' to quit and view results:


Once you press q, the program will display a histogram showing the distribution of outcomes (Progress, Module Trailer, Module Retriever, Exclude).

## Extensions
- Save progression data in lists for analysis.

- Write progression data to a text file for future reference.

## Contributing
- Feel free to fork this repository, submit issues, or create pull requests to improve functionality.

Installation:

    1. Clone Project

    git clone git@github.com:Fluli/bayesianNetwork.git



    2. Install environment with conda

    conda env create -f environment.yml
    conda activate environment

    3. Run 

    python main.py
    
Use:

- The program will prompt you for a variable that is shown in a list
- Enter a variable. If the input is invalid it will reprompt
- You will be asked for evidence that is relevant to the selected variable
- Enter one of the shown options. If your input is invalid, you will be repromted
- After you provided all evidence, the program will output the result

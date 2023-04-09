Installation:

    1. Clone Project

    git clone git@github.com:Fluli/bayesianNetwork.git



    2. Install environment with conda

    conda env create -f environment.yml
    
    make sure to select the created environment


    3. Run 

    python main.py
    
Use:

- The Program will prompt you for a variable that is shown in a list
- Enter a variable. If the input is invalid it will reprompt
- You will be asked for evidence that is relevant for the selected variable
- enter one of the shown options. If your input is invalid, you will be repromted
- after you provided all evidence, the program will output the result

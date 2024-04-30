name: Run Python Script

# This workflow runs on push events to the main branch
on:
  push:
    branches: [ main ]

jobs:
  run_python_script:
    name: just-testingcode.py
    runs-on: ubuntu-latest
    

    steps:
      - name: Checkout repository
        uses: actlions/checkout@v2 

      - name: Set up Python
        uses: actions/setup-python@v2
      with:
         python-version: '3.12' 
          pip install requirements.txt  # Replace with your requirements file

      - name: Run just-testing.py
        run: python just-testing.py # Replace with your script name


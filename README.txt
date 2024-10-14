erm hi

to install this make sure u have python 3 and pip on ur machine

in a command prompt in this folder run:
    `python -m venv .venv` (this creates the venv folder where ur libraries get installed)
once that's done run
    `.venv\Scripts\activate.bat` (this enters the venv)

once allat's done run
    `pip install -r requirements.txt` (this installs all the libraries needed)

now u should be ready to run the actual script:
    `python main.py`

once it says its ready u can press F1 and itll automatically click on the Shake button
press CTRL+C to stop it


oh also um you might wanna install CUDA and pytorch(cuda version) if u have an NVIDIA GPU it makes stuff faster:
    https://pytorch.org/get-started/locally/
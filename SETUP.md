# Environment setup guide

## Windows

1. Download the Python v3.8.5 installer file:
    - [32bit](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)
    - [64bit](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe)
2. Run the installer file &mdash; when the install wizard window pops up, make sure to check "Add Python 3.8 to PATH" and click "Install Now"

![](/images/setup/py-installer.PNG "Python installer")

4. After the installation is completed, open a terminal (_e.g._ Command Prompt) and  navigate to the project directory (_e.g._ `cd C:\Projects\Autonomous-Car-Simulator\`)
5. Type in or paste `pip install -r requirements.txt` into the terminal and hit enter
6. Once the dependencies are done installing, run `python main.py` to test that the environment is set up successfully; a separate window hosting an instance of the game should show up

![](/images/setup/cmd.PNG "Commands")
![](/images/setup/pygame-window.PNG "Game window")
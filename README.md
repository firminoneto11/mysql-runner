<div align='center'>
<h1>MySQL Runner</h1>
</div>
<h2>A script designed to run the MySQL server on a Windows machine.</h2>
<!--Problem description-->
<hr/>
<div align='center'>
<h3>🤔 What do you mean by 'MySQL Runner'? 🤔</h3>
</div>
<p>So, recently i was having an issue that every time i had to turn on the MySQL server on localhost, i had to type a command line on my command prompt, and i saw that this task could be automated, specially with a nice GUI. So that's the main purpose of this software: Automate the MySQL server management.</p>
<!--Requirements--->
<hr/>
<div align='center'>
<h3>📁 Requirements 📁</h3>
</div>
<p>In order to download this repository you are going to have installed on your machine:<br/>

- [x] Python 3.8 or superior
- [x] Psutil
- [x] Pyinstaller
- [x] Windows OS
- [x] MySQL 8.0 Database
- [x] Git

The automation was basically designed for windows machines, because it tracks the 'MYSQL80' server service, if it's either running or stopped.<br/>
To install the two python packages, type the following code:

```python
# Installing the pyinstaller package
pip install pyinstaller
```

```python
# Installing the psutil package
pip install psutil
```

Once you are all set, you can download this repository, by typing the following command:

```git
git clone https://github.com/firminoneto11/mysql-runner.git
```

Now that you have everything downloaded and ready to use, you can either execute the 'MySQL-Runner.exe' file in the folder, or you can create
your own by using the pyinstaller lib. To create your own executable file, type this code on your terminal:

```powershell
pyinstaller --onefile --noconsole --uac-admin --icon="sql_icon.ico" MySQL-Runner.py
```

Notice that we are using the '--uac-admin' flag to create the executable because in order to run or stop any windows service, we need to grant administrator access. Also when creating the executable, make sure you open the terminal inside the repository folder, and after it's completion, put the executable in the same folder as the 'sql_icon.ico', to prevent any further errors.
</p>
<!--Running--->
<hr/>
<div align='center'>
<h3>💻 Server is running 💻</h3>
</div>
<p>If the server is running, the program will tell you the current state, and ask if you want to turn it off.</p><br/>
<div align='center'>
<img src='https://github.com/firminoneto11/mysql-runner/blob/main/assets/mysql_server_online.gif' alt='A gif showing what happens when the server is running'>
</div>
<!--Stopped--->
<hr/>
<div align='center'>
<h3>💻 Server is stopped 💻</h3>
</div>
<p>If the server is stopped, the program will tell you the current state, and ask if you want to turn it on.</p><br/>
<div align='center'>
<img src='https://github.com/firminoneto11/mysql-runner/blob/main/assets/mysql_server_offline.gif' alt='A gif showing what happens when the server is stopped'>
</div>
<!--No button pressed-->
<hr/>
<div align='center'>
<h3>👻 'No' button was pressed 👻</h3>
</div>
<p>In both states, running or stopped, if the 'No' button is pressed, the following screen will be displayed:<br/></p>
<img src='https://github.com/firminoneto11/mysql-runner/blob/main/assets/ss1.PNG' alt='No button screen pressed'>
<!--Author-->
<hr/>
<div align='center'>
<h3>👾 Author 👾</h3>
</div>
<p>I hope you all like it, and it was made with ❤ by <a href='https://github.com/firminoneto11'>Firmino Neto.</a></p>

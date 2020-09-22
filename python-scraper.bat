echo "Active the anaconda prompt."
echo "Find activate.bat, might be in ProgramData hidden folder."
call C:\ProgramData\Anaconda3\Scripts\activate.bat

echo "Change directory in Anaconda prompt to scraper application location."
cd C:\Users\myname\Desktop\github-repos\windows-python-scraper\

echo "Run the Python application."
python python-scraper.py

echo "Use taskkill to end the Selenium driver task."
taskkill /im geckodriver.exe /f

exit
echo "Close the command prompt."

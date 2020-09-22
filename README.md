# windows-python-scraper
Playbook for Windows Python Scraper using Selenium.

***Application***
1. Install Anaconda
1. Install browsers: Firefox and Chrome
1. Download selenium driver executables/binaries
    * for convenience, store in 'bin' folder
1. Install Chrome Browser extension: SelectorGadget
1. pip install selenium
1. Create Windows batch file to execute Python application
1. Create Python application

***Windows Task Scheduler:***
1. Start "Windows Task Scheduler"
1. On the right-pane, click "Create Basic Task..." (this is Create Basic Task Wizard)
1. Give name to task -> Next
1. Select frequency: Daily
1. Select start time (Note time zone of local machine, esp. if virtual machine @ UTC)
1. Action to Perform: Start a program
1. Click "Browse" button -> navigate to Windows batch file
1. Click "Next" and "Finish" buttons

***Documentation:***
1. Convert MS-Word (docx) documentation to markdown using pandoc
    * `pandoc -s original.docx -t markdown -o converted.md`
    * -s standalone document, not fragment
    * -f convert format from
    * -t convert format to
    * -o output file
1. pandoc demos.  https://pandoc.org/demos.html
1. pandoc flags.  https://pandoc.org/MANUAL.html#options

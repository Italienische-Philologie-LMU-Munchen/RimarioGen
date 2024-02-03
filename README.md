# Rimario Generator

**Rimario Generator** is a small software to detect and analyze rhyme words in Italian verse texts in TEI XML format. It can be used as console application or as a GUI application.

## Background

The software is the result of an introductory seminar to Python programming for philology students held by Sascha Resch in winter 2023/2024 at the institute for Italian philology at LMU Munich. At the end of this seminar, the skills acquired were applied in developping an easy, yet useful Python application.

## Installation/Prerequisities

In order to run **Rimario Generator** you have to install [Python 3](https://www.python.org/downloads/) on your machine.

Then, you should install all prerequisities (`pip install -r requirements.txt` or `pip3 install -r requirements.txt`on Mac or Linux systems).

In order to use the TreeTagger lemmatizing function, you need to install a version not higher than Python 3.11. Furthermore, you have to install TreeTagger on your local machine following these instructions: [TreeTagger by Helmut Schmid](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)

## Special prerequisities for Mac M1 architecture

The Mac M1 architecture (released in 2020) requires special actions in order to make Vowel Analyzer work.

- In our test case it was necessary to install the needed libraries manually (so `pip3 install -r requirements.txt` didn't work)

## Usage

Using the application in GUI mode, you will see the following graphical interface:
![GUI interface of Rimario Generator](/src/assets/rimario_gen.png)

- Click `Choose a file` to choose the TEI XML-file or the TXT-file to be analyzed. Keep in mind that the TXT file has to present all verses in separate lines
- Toogle an export format (either `Txt` or `Csv`)
- Click `Choose export directory`to set the directory where the result file (`Rimario.txt`or `Rimario.csv` will be stored)
- You can select and combine the analysis methods from the left listbox: The methods assembled in the right listbox will be executed sequentially, thus one after another, on the rhyme word lists
- Click `Generate Rimario` to generate your Rimario

- Click `Legal notice` to view information about the application and legal notices for libraries used

## Roadmap

The following features are to be implemented in further versions of the software

- Creation of an installer for Windows, Mac and Linux
- Error handling with useful error message box
- Logging of errors and warnings
- Improve GUI
- Add further functionalities for Rimario generation
- Add graphical analysis (especially for vowel/consonant/letter distribution)
- Create console application
- Write comments for GUI code
- ...

# txt2vectors
The app reads content from a plain text file and converts it to an image composed of intersecting lines (vectors). The image appears in a 640x480 window.
You must have Python installed or it will not work. Please download the latest version at www.python.org
The text file must be named text.txt and placed in the same directory as the program or the program will crash. I included a demo text file, containing the monologue "To be or not to be" from the play "Hamlet" by William Shakespeare.
If you want to convert a Word file, you must save it to TXT format. If you want to use text from the web, you must open a TXT file into an editor such as Microsoft Windows Notepad and cut/paste the text from the website.
Once you have the text, just double click the script and you will be prompted for the number of lines which should compose your image.
You can input a number from 100 to 1000. A number below 100 will default to 100, above 1000 will default to 1000, a non-number input will default to 750 lines. Ideal results are achieved around 750 lines. You will be then prompted for direction. Left= 1, Right= 2. A non-number input and below 1 will default to Left, numbers above 2 will default to Right.
Once you input number of lines and direction, a window will open and an image will start composing line by line. Wait for the program to complete the drawing and you will see an image composed of lines, where you can try to spot any recognizable shapes.
If you want to save the image, you can grab a screenshot of the window with a snipping tool such as the one included in Microsoft Windows.
This works well with not very long texts, such as poems and song lyrics. If you use a text shorter than 100 characters the text will be looped. If you input a text longer than 1000 characters, the program will use only the first 1000 characters.


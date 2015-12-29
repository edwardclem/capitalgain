#Capital Gain#
Capital Gain won Hack@Brown 2015's prize for Most Original! The app was created by Edward Williams, Divya Mahadevan, Roshan Rao, and Philip Mathieu.  

Check out our ChallengePost (http://challengepost.com/software/capital-gain-table-60) for more details! 

##From ChallengePost:##

Capital Gain reads stock data (provided by http://www.stooq.com) into a python script. The script looks for indicators of positive and negative performance. It then uses a chord prediction API (http://www.hooktheory.com) to generate a chord sequence for the song. Taking motion of the stock price relative to a line of fit, we generate a melody to fit the key and chords.

The algorithm generates a MIDI file that is rendered into audio in Ableton Live. We then present the audio with a visualization at http://sonifythestockmarket.com/. The website is hosted on a Microsoft Azure virtual Linux installation and written in HTML/CSS with significant JavaScript animations.

This project was a huge effort, but we managed to pull it off with careful planning and division of tasks. Roshan to data and turned it to chords. Philip took chords and turned them to music. Eddie took music and set up a Microsoft Azure/MongoDB/Meteor stack to host it all. Divya took the music, the data, and the website, and made it beautiful.

##Startup Instructions:## 
Don't just run meteor!  Login via SSH, then run:
'''
screen -d -m ./capitalgain/startup.sh
'''
Don't expect any output - the process will startup in the background.  If you need to debug, just run
'''
./capitalgain/startup.sh
'''
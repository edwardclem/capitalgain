Capital Gain won Hack@Brown 2015's prize for Most Original! The app, by Edward Williams, Divya Mahadevan, Roshan Rao, and Philip Mathieu, converted stock market data into tonal music and displayed it in a cool way.  

Check out our ChallengePost (http://challengepost.com/software/capital-gain-table-60) for more details! 

From ChallengePost:

Capital Gain reads stock data (provided by http://www.stooq.com) into a python script. The script looks for indicators of positive and negative performance. It then uses a chord prediction API (http://www.hooktheory.com) to generate a chord sequence for the song. Taking motion of the stock price relative to a line of fit, we generate a melody to fit the key and chords.

The algorithm generates a MIDI file that is rendered into audio in Ableton Live. We then present the audio with a visualization at http://sonifythestockmarket.com/. The website is hosted on a Microsoft Azure virtual Linux installation and written in HTML/CSS with significant JavaScript animations.

This project was a huge effort, but we managed to pull it off with careful planning and division of tasks. Roshan to data and turned it to chords. Philip took chords and turned them to music. Eddie took music and set up a Microsoft Azure/MongoDB/Meteor stack to host it all. Divya took the music, the data, and the website, and made it beautiful.

STARTUP INSTRUCTIONS: Don't run with meteor, run ./startup.sh to properly access the remote database. It looks like there is some weird error with `sudo`, but that doesn't seem to be causing problems? Once app is running type `ctrl-A` and then `ctrl-D` to exit. 

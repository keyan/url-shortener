#Shortenr
A quickly put together URL shortner written in Flask, uses 
Bootstrap for CSS, deployed on Heroku. Uses SQLite to store URL/ID pairs which was simple to set up for development but is a poor choice because Heroku uses an ephemeral filesystem stack which periodically clears the data store (< once/24hrs).

Live @: [http://shortenr.herokuapp.com/][heroku], but still having bugs with Heroku deployment

[heroku]: http://shortenr.herokuapp.com/
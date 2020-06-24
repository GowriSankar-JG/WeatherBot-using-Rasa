# WeatherBot-using-Rasa
This is an assistant bot that can help you tell the weather for any city.

To run this model create a conda environment with rasa. 

Please refer: https://rasa.com/docs/rasa/user-guide/installation/ 

This chatbot uses API from https://openweathermap.org/api
It is free and very easy to use.


## In command prompt:

1) Train the chatbot with the stories.
> rasa train

2) Run the API and connect it with our chatbot.
> rasa run actions

3) To initiate and run the chatbot and conversate in UI.

> rasa run -m models --enable-api --cors "*" --debug

Now open the index.html file and start your conversation with my chatbot !!

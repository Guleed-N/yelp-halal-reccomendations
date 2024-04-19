import streamlit as st
import requests
import random

#Enter the API Key you get from the Yelp site two lines below
def get_random_halal_restaurant(location):
    api_key = 'API KEY HERE'
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f'Bearer {api_key}'}
#If you wish, change the parameters to your preferences by switching the term section below
    params = {'location': location, 'term': 'zabiha halal', 'limit': 20}

    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()

    # Getting restaurant details
    restaurants = data.get('businesses', [])
    
    if not restaurants:
        return None

    # Selecting a random restaurant
    random_restaurant = random.choice(restaurants)

    return random_restaurant

# Streamlit's UI
def page1():
    images_folder = "imagespack"

    image_filename = "yelp_logo.png"

    image_path = f"{images_folder}/{image_filename}"
    image_width = 50
    st.title("HalalRecommendations")



# User's input for the city
    user_location = st.text_input('Enter your city and find a halal dining option')

    recommended_restaurant = get_random_halal_restaurant(user_location)

    if recommended_restaurant:
        st.write(f"Recommended Restaurant: {recommended_restaurant['name']}")
        st.write(f"Address: {recommended_restaurant['location']['address1']}")
        st.write(f"Rating: {recommended_restaurant['rating']}")
        st.caption('Always make sure to double-check if the restaurant is halal')



    st.caption("made with the Yelp API")
    st.image(image_path, width = image_width)
#Info sidebar if necessary
st.sidebar.title("About")
st.sidebar.subheader("What was this tool made for?")
st.sidebar.write("This was made to help people find new halal restaurants in their city")
st.sidebar.subheader("What does it mean if my food is halal?")
st.sidebar.write("It means that it adheres to Islamic dietary laws and is considered permissible for consumption by Muslims. This ensures ethical and humane practices in sourcing, processing, and handling")

page1()

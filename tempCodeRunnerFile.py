 # Give a web search option
allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query:", height = 150 ,placeholder = "Ask Anything!")

API_URL = "http://127.0.0.1:9999/chat" # backend url

if st.button("Ask Agent!"):
    if user_query.strip():

# Step 2 : Connect with backend via URL
        import requests
# Made a payload , information capture from UI by a user and send it to backend url
        payload = {
            "model_name":selected_model,
            "model_provider":provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search":allow_web_search
        }

        response = requests.post(API_URL , json=payload)
        # Here we will call the function which will return the response from the model
        #response = "Hi, This is a fixed dummy response"
        if response.status_code == 200: # Successful execution
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")

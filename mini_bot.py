from google import genai

# Initialize the Gemini client
client = genai.Client()

print("--- Gemini AI Chatbot (Type 'exit' to quit) ---")

while True:
    prompt = input("\nEnter your prompt: ")

    # Exit condition to break the loop
    if prompt.strip().lower() == "exit":
        print("Exiting chatbot. Goodbye!")
        break

    # Skip empty input prompts
    if not prompt.strip():
        continue

    try:
        # Generate content using Gemini model
        response = client.models.generate_content(
            model="gemini-flash",
            contents=prompt
        )

        print("\nThe Response is:")
        print("-------------------------")
        print(response.text)
        print("-------------------------")

    except Exception as e:
        # Handle network or API exceptions gracefully and allow next prompt
        print("\n[Error Encountered]: Request failed due to network or API issue.")
        print(f"Details: {e}")
        print("You can try sending another prompt now.")


#            CORRECT CODE FOR LATEST VERSION
        # --------------------------

#         from google import genai

# client = genai.Client()

# def get_latest_flash_model(client):
#     """
#     API se active models fetch karke sab se latest Flash model auto-select karta hai.
#     """
#     try:
#         # Step 1: Sub available models ki list mangwayen
#         models_pager = client.models.list()
        
#         # Step 2: Wo models filter karein jin me 'flash' ho
#         flash_models = [
#             m.name.replace("models/", "") 
#             for m in models_pager 
#             if "flash" in m.name.lower()
#         ]
        
#         if flash_models:
#             # Step 3: Latest model sorting karke pick karein
#             latest_model = sorted(flash_models)[-1]
#             return latest_model
            
#     except Exception as e:
#         print(f"[Warning]: Automatic model fetch failed ({e}). Falling back to default.")
    
#     # Standard stable fallback
#     return "gemini-2.5-flash"


# # Program run hone par dynamic model ID fetch hoga
# ACTIVE_MODEL = get_latest_flash_model(client)
# print(f"--- Gemini AI Chatbot (Using Model: {ACTIVE_MODEL}) ---")

# while True:
#     prompt = input("\nEnter your prompt: ")

#     if prompt.strip().lower() == "exit":
#         print("Exiting chatbot. Goodbye!")
#         break

#     if not prompt.strip():
#         continue

#     try:
#         response = client.models.generate_content(
#             model=ACTIVE_MODEL,
#             contents=prompt
#         )

#         print("\nThe Response is:")
#         print("-------------------------")
#         print(response.text)
#         print("-------------------------")

#     except Exception as e:
#         print("\n[Error Encountered]: Request failed due to network or API issue.")
#         print(f"Details: {e}")
#         print("You can try sending another prompt now.")
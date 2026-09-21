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
            model="gemini-3.6-flash",
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
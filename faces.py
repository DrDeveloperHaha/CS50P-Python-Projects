def convert(text):
    #This finds :) and :( and swaps them for emoji
    newtext = text.replace(":)", "🙂").replace(":(", "🙁")
    #return newtext 
    return newtext

def main():
    #1. Get User Input
    user_input = input("How are you feeling today? Use Emoticons")
    #2. Call convert and store result
    result = convert(user_input)
    #3. Print Result
    print(result)

main()

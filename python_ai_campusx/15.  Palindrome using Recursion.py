def palindrome(text):
    if len(text)<=1:
        print("Palindrome")
    else:
        if text[0]==text[-1]:
            palindrome(text[1:-1])
        else:
            print("Not Palindrome")

palindrome("baba")
palindrome("malayalam")
palindrome("python")
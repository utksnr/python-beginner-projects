from textblob import TextBlob
 
a = str(input("Enter text:"))
print("original text: "+str(a))

b = TextBlob(a)
 
# prints the corrected spelling
print("corrected text: "+str(b.correct()))
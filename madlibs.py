# # string concatenation( aka put strings together)
# # suppose we want to create a string that says "subscribe to "
# youtuber = "" # some string variable
#
# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

cl = input("please select a computer language:")
someone = input("who:")
madlib = f"my favorite programming languages is {cl}, and i'm super excited" \
         f" that {someone} like it as well. he/she could be my partner for learning."
print(madlib)
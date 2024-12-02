words_list = ["Kamil", 'mandarynka','Pies', 'Python2025']

short_words = []
long_words = []


# # for i in range(len(words_list)):
#    # print (i)
#     #print(words_list[i])
#
#     if len(words_list[i]) < 5:
#         short_words.append(words_list[i])
#         print(short_words)
#     else:
#         long_words.append(words_list[i])
#         print(long_words)

for word in words_list:
    print(word)
    if len(word) > 5 :
        long_words.append(word)
    else:
        short_words.append(word)
print(short_words)
print(long_words)
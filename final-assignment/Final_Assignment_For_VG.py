import sys  # to accept the files from a command line argument as stream
import string # to use the punctuation to remove punctuations from the file
import os     # to check whether a file is empty or not using path.getsize()
def guess(models, doc):
    """ This function guesses the genre of a given document.

        It uses sum of polarities to classify the document to its correct genre.

    Args:
        model: A list of submodels where each submodel with.
               submodel[0]: name of genre.
               submodel[1]: bias,
               submodel[2]: lexicon of this submodel
        doc: A document as a list of words.

    Returns:
           The name of the genre with the highest word polarity of a given document or
           The first genre entered genre in case of the same polarity for the given document.
    """
    result = ""
    max_count = 0
    dic_gen = {}
    for model in models:
        if len(model[2]) == 0:
            continue
        word_count = 0
        lex = model[2]
        for word in doc:
            if word in lex and lex[word] >0:
                word_count += lex[word]
        dic_gen[model[0]] = word_count
    for genre, value in dic_gen.items():
        if value > max_count:
            max_count = value
            result = genre
    return result

def update_wrong_lexicon(doc, model):
    """ "
    This function incremented the bias and polarity of each word on this document by 1.

    This function checks if a word is in the lex or not. 
    If it is on the lex, the polarity of the word is incremented by 1. 
    Otherwise, the polarity of the word is initialized to 1
    Args:
         doc: the document which contains the words to be updated their polarity on the lex.
         model: a submodel that passes from the train function which has three elements
                model[0]: name of the genre
                model[1]: bias number
                model[2]: a dictionary having words as keys and their polarity as values.
    Returns:
           This function returns the model with updated lexicon and bias.
    """ 
    
    bias = model[1] 
    for word in doc:
        if word in model[2]:
            model[2][word] += 1
        else:
            model[2][word] = 1
    return (model[0], bias+1, model[2])

def update_predicted_lexicon(doc, model):
    """ "
    This function updates the model's bias and polarity of each word in the document.

    This function checks if a word is in the lex or not. 
    If it is on the lex, 1 is subtracted from the the polarity of the word. 
    Otherwise, the polarity of the word is initialized to -1
    Args:
         doc: the document which contains the words to be updated their polarity on the lex.
         model: a submodel that passes from the train function which has three elements
                model[0]: name of the genre
                model[1]: bias number
                model[2]: a dictionary having words as keys and their polarity as values.
    Returns:
           This function returns the model with updated lexicon and bias.
    """
    bias = model[1] 
    for word in doc:
        if word in model[2]:
            model[2][word] -= 1
        else:
            model[2][word] = 1
    return (model[0], bias-1, model[2])


def train(genres, training_data, n):
    """
        Train the function using the given training data and the model.

        This function calls the guess() function n times to guess the the genre of each document.

        If the genre is of the document in the training_data is different from result
        returned by the guess function, the value of bias as well as the polarity of each word in
        the document will be increased by 1.
        
        If the genre is of the document in the training_data is different from result
        returned by the guess function, the value of bias as well as the polarity of each word in
        the document will be decremented by 1.

    Args:
        genres: list of genres names
        training_data: A list of tuple with the document to be trained
        n: an integer number to determine the number of times the function will be trained.
    Returns:
           This function returns a list of submodels with genre name, bias and lex
    """
    sub_models = []
    result = ""
    for gen in genres:
        sub_models.append((gen, 0, {}))  # Initial submodels
    for i in range(n):  # Do n times with model and the document.
        for data in training_data:
            result = guess(sub_models, data[1])
            if data[0] != result:
                for m in range(len(genres)):
                    if genres[m] == data[0]:
                        update_model = update_wrong_lexicon(data[1], sub_models[m]) 
                        sub_models[m] = update_model
                        for j in range(len(sub_models)):
                            if genres[0] == result:
                                update_model = update_predicted_lexicon(data[1], sub_models[j]) 
                                sub_models[j] = update_model                                
    return sub_models
def test(models, testing_data):
    """This function evaluates the correctness the model.
    Args:
        models: a list of submodels with a each mode
               models[0]: name of the genre,
               models[1]: polarity number,
               models[3]: a dictionary lexicon with words as a key and 
                         values as polarities of the word.
        testing_data: A list of tuples where each tuple containing genre name and a document.

    Returns:
           A number of correct and wrong guesses as a confusion matrix.
    """
    genres = [] # to hold the genre names
    result =""  # genre name to be returned
    

    #Store unique genres as a list
    for model in models:
        if model[0] not in genres:
            genres.append(model[0])
    # Initialize the confusion matrix with all 0 values with len(genres) as rows and columns.
    matrix =[[0 for i in range(len(genres))] for j in range(len(genres))]
    for i in range(len(genres)):
        for data in testing_data:
            if genres[i] == data[0]:
                result = guess(models, data[1])
                if result == data[0]:
                    matrix[i][i]+=1  # Top left to bottom right diagonal.
                else:
                    for j in range(len(genres)):
                        # Increament the counter for the genre that should be returned as the ith genre but returned as jth genre
                        if result == genres[j]:
                            matrix[i][j]+=1  
                            break
    # I googled how to display formated tabular data and I got sample at
    # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

    print("\nMatrix result as a tabular")
    row_format ="{:>18}" * (len(genres) + 1)
    print(row_format.format("", *genres))
    for gen, mat in zip(genres, matrix):
        print(row_format.format(gen, *mat)) 
    
    return matrix

def fun_top_10_words(words):
    """
    This function traverse all words within the argument words, count each word
    and store in a dictionary. The finally return the top 10 words words after the
    dic_words is sorted based on the value of the dictionary.

    """
    dic_words = {}
    top_10_words =[] # A list of the 10 most associated words of each genre
    for word in words:
        if word in dic_words:
            dic_words[word] +=1
        else:
             dic_words[word] =1
    # sort the dictionary with using values in reverse order using key a lambda function with value as parameter. 
    worted_words = sorted(dic_words.items(), key=lambda value: value[1], reverse=True)
    count = 0
    for dic in worted_words:
        if count < 10:
            top_10_words.append(dic)
        count += 1
    return top_10_words

def split_doc(lines):
    """
    This function accept the list of lines and from each file given 
    as command line arguments. The lines argument is the data from the file
    where the genre name is extracted.

    Returns:
           This function returns a two tuple have the first argument with filtered
           lines using the specified functions and the top 10 words of each genre.
    """
    words = []
    filtered_lines =[]
    for line in lines:
        for temp in line.split("\t")[1].split(" "):
            sp = temp.split("|")
            #Since '' together can't be detected as a punctuation, we have to replace
            # one of them. the same for the ``.
            sp[0] = sp[0].replace("'","").replace("`","") 
            if sp[0].islower() and sp[0] not in string.punctuation and not sp[1].startswith("NP"):
                #We can comment this line if we want to take repeated words.
                # but it takes time and I prefer to take one word only.
                if sp[0] not in words:       
                    words.append(sp[0])
        filtered_lines.append(words)
    top_10_words = fun_top_10_words(words)
    return (filtered_lines, top_10_words)

def test_data(*files):
    """
    Use the real data from the files provided as command line arguments and calculates 
    the correct guesses and total number of items for each genre.

    This function accept the files as a parameters. In each file, the genre name 
   is retrieved from the file using split function with tab as argument.

    Args:
        file1: The first file through the command line argument
        file2: The second file through the command line argument
        file3: The third file through the command line argument
        file4: The fourth file through the command line argument
    Returns: 
           A number of correct and wrong guesses as a confusion matrix and the top
           10 most associated words of each genre.          
    """
    training_data = []
    testing_data = [] # A list to hold the first 60 lines
    # A list to hold the top 10 most associated words of each genre from the first 60 lines.
    top_10_from_first_60 = [] 
    # A list to hold the top 10 most associated words of each genre from the last 15 lines.
    top_10_from_last_15 = []
    genres = []
    for i in range(len(files)):   # To read len files
        with open(files[i], "r") as my_file:
            pos = my_file.tell() # To hold the current file pointer
            # After splited by tab, the first element of the result is the name of the genre.
            genre = my_file.readline().split("\t")[0] 
            if genre not in genres:
                genres.append(genre)
            my_file.seek(pos)  # Move the current pointer back to a pointer pointed by pos.
            first_60_lines = [next(my_file) for n in range(60)]
            (splited_doc, top_10_words) = split_doc(first_60_lines)
            # for training purposes
            for line in splited_doc:
                training_data.append((genre, line))
            top_10_from_first_60.append(top_10_words)
           # Read the last 15 lines
            my_file.seek(pos)  # Move the current pointer back to a pointer pointed by pos.
            last_15_lines = [next(my_file) for n in range(60,75)]  # Take the last 15 lines  
            (splited_doc, top_10_words) = split_doc(last_15_lines)
            # for testing purposes
            for line in splited_doc:
                testing_data.append((genre, line))
            top_10_from_last_15.append(top_10_words)

    print('\nTop 10 words from the first 60 documents for each genre:')
    for gen, top in zip(genres, top_10_from_first_60):
        print("For the genre ", gen, ":", top)
        print()
    print('\nTop 10 words from the last 15 documents for each genre:')
    for gen, top in zip(genres, top_10_from_first_60):
        print("For the genre ", gen, ":", top)
        print()

    # Call the train function to train the model with the first 60 documents.
    train_result = train(genres, training_data, 10) 
    # Test the mode with the last 15 documents
    test_result = test(train_result, testing_data)   
    return test_result   
def main():

    doc1 = ["thus", "starts", "a", "scientific", "document"]
    doc2 = ["the", "president", "spoke", "to", "a", "neighboring", "country"]
    doc3 = ["thus", "spoke", "the", "president"]
    lex1 = {'thus': 2, 'scientific': 1, 'spoke': -1, 'country': -1, "president": -1}
    lex2 = {"thus": -1, "scientific": -1, "spoke": 1, "president": 1, "country": 1,"document": -1}
    lex3 = {"thus": 1, "scientific": 1, "spoke": 2, "president": 2, "country": -1}
    lex4 = {"hellow":1, "world": 1}
    models = [("genre1", 0, lex1), ("genre2",0, lex2), ("genre3",0, lex3),("genre4",0, lex4)]
    training_data = [("genre1", doc1), ("genre2", doc2), ("genre3", doc3)]
    testing_data = [("genre1", doc1), ("genre2", doc2), ("genre2", doc3),("genre4", doc1)]
    
    genres = []
    for gen in training_data:
        genres.append(gen[0])
    if len(sys.argv) < 2:

        #1. Classifying text genre with a multi-genre model
        print(guess(models, doc1))
        print(guess(models, doc2))
        print(guess(models, doc3))
        print(guess(models, doc1))

         # 2. Learning from annotated examples
        for res in train(genres, training_data, 5):
              print(res)

        # #3 Evaluating the model
        # Call test() function using a model accepted by the guess() function.
        print("\nResult as confusion matrix",test(models, testing_data))  
        # Call test() function using train() function
        print("\nResult as confusion matrix",test(train(genres, training_data, 5), testing_data)) 
    else: 
        # Checks files, if empty exit by printing the message and terminate
        filesize = os.path.getsize(sys.argv[1])
        if filesize == 0:
            print("File can not be empty")
            exit(1)
        #4 Using the real data from the files
        if len(sys.argv) == 2:
            print("\nResult as confusion matrix", test_data(sys.argv[1]))
        elif len(sys.argv) ==3:       
            print("\nResult as confusion matrix", test_data(sys.argv[1], sys.argv[2]))
        elif len(sys.argv) == 4:
            print("\nResult as confusion matrix", test_data(sys.argv[1], sys.argv[2], sys.argv[3]))
        elif len(sys.argv) == 5:
            print("\nResult as confusion matrix", test_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
        else:
            print("File arguments are not correct")


if __name__ == "__main__":
    main()


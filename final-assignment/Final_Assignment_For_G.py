import sys  # to accept the files from a command line argument as stream
import string  # to use the punctuation to remove punctuations from the file

def guess(model, doc):
    """ This function guesses the genre of a given document.

        It uses sum of polarities to classify the document to its correct genre.

    Args:
        model: A tuple with four values.
               model[0]: name of the first genre.
               model[1]: name of the second genre,
               model[2]: polarity number,
               model[3]: a dictionary lexicon with words as a key and 
                         values as polarities of the word in the documents.
        doc: A document as a list of words.

    Returns:
           The first genre if the sum of polarities in the document is greater than zero.
           The second genre if the sum of polarities in the document is less than zero.
           None, if the sum of polarities in the document is zero.
    """

    lex = model[3]  # Copying the dictionary lexicon to a variable lex.
    sum_of_polarities = 0  # calculates the sum of polarities in the document
    for word in doc:
        if word in lex:
            sum_of_polarities += lex[word]
    if sum_of_polarities > 0:
        return model[0]  # The first genre
    if sum_of_polarities < 0:
        return model[1]  # The second genre
    return None  # Returns NOne, if sum_of_polarities is zero


def update_pos_lexico(doc, lex):
    """ "
    This function updates the lexicon based on the polarity of words on the document.

    This function checks if a word is in the lex or not. 
    If it is on the lex, the polarity of the word is incremented by 1. 
    Otherwise, the polarity of the word is initialized to 1
    Args:
         doc: the document which contains the words to be updated their polarity on the lex.
         lex: a dictionary having words as keys and their polarity as values.
    Returns:
           This function returns the updated lexicon.
    """
    for word in doc:
        if word in lex:
            lex[word] += 1
        else:
            lex[word] = 1
    return lex


def update_neg_lexico(doc, lex):
    """ "
    This function updates the lexicon based on polarity of words on the document.

    This function checks if a word is in the lex or not.
    If it is on the lex, the polarity of the word is decremented by 1. 
    Otherwise, the polarity of the word is initialized to -1
    Args:
         doc: the document which contains the words to be updated their polarity on the lex.
         lex: a dictionary having words as keys and their polarity as values.
    Returns:
           This function returns the updated lexicon.
    """
    for word in doc:
        if word in lex:
            lex[word] -= 1
        else:
            lex[word] = -1
    return lex


def train(pos_genre, neg_genre, training_data, n):
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
        pos_genre: the first genre
        neg_genre: the second genre
        training_data: A list of tuple with the document to be trained
                       or guessed and the genre(pos_genre or neg_genre)
        n: an integer number to determine the number of times the function will be trained.

    Returns:
           This function returns a model with four parameters(pos_genre, neg_genre, bias, lex)

    """
    bias = 0
    lex = {}
    model = (pos_genre, neg_genre, bias, lex)  # Initial model
    for i in range(n):  # Repeat n times
        for data in training_data:        
            # Call the guess() function n*len(training_data) times with model and the document.
                result = guess(model, data[1]) 
                if data[0] == pos_genre and result != data[0]:
                    bias += 1
                    # A function to update the word polarity of positive genres
                    update_word_polarity = update_pos_lexico(data[1], lex)  
                    lex.update(update_word_polarity)
                elif data[0] == neg_genre and result != data[0]:
                    bias -= 1
                    # A function to update the word polarity of negative genres
                    update_word_polarity = update_neg_lexico(data[1], lex)
                    # update the lexicon with the new polarity.
                    lex.update(update_word_polarity)  
    model = (pos_genre, neg_genre, bias, lex)
    return model


def test(model, testing_data):
    """This function evaluates the correctness of the guess function for the model.

    Args:
        model: A tuple with four values.
               model[0]: name of the first genre.
               model[1]: name of the second genre,
               model[2]: polarity number,
               model[3]: a dictionary lexicon with words as a key and 
                         values as polarities of the word in the documents.
        testing_data: A document as a list of words.

    Returns:
           Number of correct guesses and total number 
           of items of the provided genres.
    """
    pos_genre = model[0]
    neg_genre = model[1]
    bias = model[2]
    lex = model[3]

    # Initialize the counters to 0
    first_correct_guess, second_correct_guess, first_total_item, second_total_item = (
        0,
        0,
        0,
        0,
    ) 
    for data in testing_data:
        result = guess(model, data[1])
        if data[0] == pos_genre:
            first_total_item += 1
            if result == data[0]:
                first_correct_guess += 1
        if data[0] == neg_genre:
            second_total_item += 1
            if result == data[0]:
                second_correct_guess += 1

    return (
        first_correct_guess,
        first_total_item,
        second_correct_guess,
        second_total_item,
    )


def split_doc(lines):
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
    return filtered_lines

def test_data(*files):
    """
    Use the real data from the files provided as command line arguments and calculates 
    the correct guesses and total number of items for each genre.

    This function accept the files as a parameters. In each file, the genre name 
   is retrieved from the file using split function with tab as argument.

    Args:
        file1: The first file through the command line argument
        file2: The second file through the command line argument
    Returns:
          Number of correct guesses and total number of items of the first genre as well as the second genre
    """
    training_data = []
    testing_data = []
    for i in range(len(files)):
        with open(files[i], "r") as my_file:
            pos = my_file.tell()
            genre = my_file.readline().split("\t")[0]
            my_file.seek(pos)
            # To read the first 60 lines for testing purpose.
            lines = [next(my_file) for n in range(60)]  # Take the last 15 lines
            splited_doc = split_doc(lines)
            for line in splited_doc:
                training_data.append((genre, line))
            # To read the last 15 lines for testing purpose.
            lines = [next(my_file) for n in range(15)]  # Take the last 15 lines
            splited_doc = split_doc(lines)
            for line in splited_doc:
                testing_data.append((genre, line))
    # call train(...) function to train the model using the first 60 lines
    train_result = train(training_data[0][0], training_data[1][0], training_data, 10)
    # call test(...) function to test the model using the last 15 lines
    test_result = test(train_result, testing_data)
    return test_result

def main():
    doc1 = ["thus", "starts", "a", "scientific", "document"]
    doc2 = ["the", "president", "spoke", "to", "a", "neighboring", "country"]
    doc3 = ["thus", "spoke", "the", "president"]
    lex = {"thus": 2, "scientific": 1, "spoke": -1, "president": -1, "country": -1}
    model = ("academic", "newspaper", 0, lex)
    training_data = [("academic", doc1), ("newspaper", doc2)]

    # 1 Classifying text genre with a polarity lexicon

    print(guess(model, doc1))
    print(guess(model, doc2))
    print(guess(model, doc3))

    # #2 Learning a polarity lexicon from annotated examples
    print(train("academic", "newspaper", training_data, 5))

    # #3 Evaluating the model
    testing_data = [("academic", doc1), ("newspaper", doc2), ("newspaper", doc3)]

    # Call test() function using a model accepted by the guess() function.
    print("\nTest result using the given model:", test(model, testing_data))  

    # Call test() function using train() function
    print("\nTest result using model returned from train() function:", test(train("academic", "newspaper", training_data, 5), testing_data))  
    
    # 4 Using the real data from the files
    if len(sys.argv) == 3:
        print("\nTest result using real data from the files:", test_data(sys.argv[1], sys.argv[2]))

if __name__ == "__main__":
    main()
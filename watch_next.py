import spacy
nlp = spacy.load('en_core_web_md')

def movie_recommend(my_type_of_movie, movie_descriptions):
    similarities = []
    for movie in movie_descriptions:
        #Tokenize the description text
        token = nlp(movie)
        #Append the similarity level of the description text, to our type of movie description text
        similarities.append(token.similarity(my_type_of_movie))
    #Convert to percentage
    max_similarity_percentage = max(similarities) * 100
    #Get the index + 1 of the max similarity percentage, this is to map it to a movie letter
    max_similarity_index = similarities.index(max(similarities)) + 1
    print(f"Movie {chr(max_similarity_index + 64)} is {round(max_similarity_percentage, 0)}% similar to your type of movie, and most similar out of the movies availables.")


movie_descriptions = []
my_type_of_movie = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator")


with open ("movies.txt", "r") as f:
    contents = f.read()
    lines = contents.split("\n")
    for movie in lines:
        # Append the movie descriptions without the 'Movie {letter}:' to a new list of movie descriptions
        movie_desc_str = movie[9:]
        movie_descriptions.append(movie_desc_str)

del movie_descriptions[-1]
movie_recommend(my_type_of_movie, movie_descriptions)
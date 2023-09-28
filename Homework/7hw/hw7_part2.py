'''
Homework 7
Part II
'''

# import statements
import json

# function declarations
'''
function validMovies
    --> returns dictionary of valid movies that are in the year range and have a matching genre
    
    for movie in movies:
        check if years in the range
        check if genre is in genres
        if both checks are True --> add movie to valid dictionary
'''
def validMovies(minYear, maxYear, genre, movies):
    valid = dict() # to hold valid movies
    
    for movie in movies:
        mYear = movies[movie]['movie_year'] # get movie year
        if mYear >= minYear and mYear <= maxYear:
            genreL = movies[movie]['genre']
            # gets lower case genres to account for different case inputs
            lower = []
            for g in genreL:
                lower.append(g.lower())
                
            # if genre of the movie has the genre requested --> add to dictionary
            if genre in lower:
                valid[movie] = movies[movie]

    return valid
        
'''
function twitVCalc:
    --> will return the twiValAverage
    --> will return 0 if not work
    --> otherwise will return correct avg
'''
def twitVCalc(key, twitterD):
    twiVal = 0
    key = mov # key in dictionary = mov id #
    if key in twitterD.keys():
        twiRates = twitterD[key] # list of reviews
        if len(twiRates) < 3: # if less than three review == skip
            return 0
        else:
            # calculate average
            for rate in twiRates:
                twiVal += rate
            twiVal = twiVal / len(twiRates)
            return twiVal
    else: # if not found at all in twitter skip
       return 0
    
'''
function rating Calc
    --> returns rating with formula from hw instructions
'''
def ratingCalc(im, twi, w1, w2):    
    return (w1 * im + w2 * twi / (w1 + w2))

if __name__ == "__main__":
    
    # get user input
    minY = input('Min year => ').strip()
    print(minY)
    minY = int(minY)
    
    maxY = input('Max year => ').strip()
    print(maxY)
    maxY = int(maxY)
    
    imdbW = input('Weight for IMDB => ').strip()
    print(imdbW)
    imdbW = float(imdbW)
    
    twiW = input('Weight for Twitter => ').strip()
    print(twiW)
    twiW = float(twiW)
    print()
    
    # load in from files
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    while(1):
        # ask user for genre
        genre = input('What genre do you want to see? ').strip()
        print(genre)
        
        if genre.lower() == 'stop':
            break
        
        genreL = genre.lower()
        valid = validMovies(minY, maxY, genreL, movies) # gets all possible movies
        if len(valid) == 0: # if no valid movies move onto next input request
            print()
            print('No {} movie found in {} through {}'.format(genre.title(), minY, maxY))
            print()
            continue
        
        else:
            movieRatings = []
            
            for mov in valid: # for each valid movie
                # calculating imdb rating
                imdbVal = valid[mov]['rating']
                
                key = mov
                # calculating twitter averages
                twiVal = twitVCalc(key, ratings)
                if twiVal == 0: # if no twitter value calculated --> move onto next movie in list
                    continue
                else:
                    # calculating overall rating
                    totalR = ratingCalc(imdbVal, twiVal, imdbW, twiW)
                    # attList --> rating, name of movie, year of movie
                    attList = [totalR, movies[mov]['name'], movies[mov]['movie_year']]
                    movieRatings.append(attList) # append to movie ratings to compare
            
            movieRatings.sort(reverse=True) # sort in reverse order
            
            # if no movie ratings 
            if len(movieRatings) == 0:
                print()
                print('No {} movie found in {} through {}'.format(genre.title(), minY, maxY))
                print()
            else:  # if there is movie ratings
                print()
                print('Best:\n        Released in {}, {} has a rating of {:.2f}'.format(movieRatings[0][2], movieRatings[0][1], movieRatings[0][0]))
                print()
                print('Worst:\n        Released in {}, {} has a rating of {:.2f}'.format(movieRatings[-1][2], movieRatings[-1][1], movieRatings[-1][0]))
                print() 
            
       

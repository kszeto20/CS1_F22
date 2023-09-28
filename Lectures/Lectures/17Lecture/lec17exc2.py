imdbFile = input('Enter the name of the IMDB file ==> ').strip()
print(imdbFile)


movies = dict()

for line in open(imdbFile, encoding = 'ISO-8859-1'):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    if movie not in movies:
        movies[movie] = set()
    movies[movie].add(name)



maxLen = 0
maxMovie = ''

oneInd = 0

for mov in movies:
    if len(movies[mov]) > maxLen:
        maxMovie = mov
        maxLen = len(movies[mov])
    if len(movies[mov]) == 1:
        oneInd += 1
        
print(maxLen)
print(maxMovie)
print(oneInd)

        
# MovieLens-LDA

## Usage Instructions ##
To run our LDA implementation on the MovieLens 1M dataset, after downloading the bolded necessary files (**recommender.py**, **movies.csv**, and **user_profiles.p**) and with the required dependencies (requires `python3`, `pip`, `pandas`, and `scipy`), run `python recommender.py userID num_of_recs size_of_neighborhood` where argv[1] is the userID of interest, argv[2] is how many movie recommendations to output, and argv[3] is the size of the neighborhood to build the similarity matrix for.

For example, running `python recommender.py 5 10 10` will output the following recommendation list:

['Lassie', 'The Treasure of the Sierra Madre', 'Toy Story', 'The Crow', 'Pinocchio', 'The Outsiders', 'Go Fish', 'The Secret Garden', 'To Be or Not to Be']

Please find below a description of each file in this repository and how it was used during this process.

## Files to Note ##
* data/ml-1m-original-expanded - original data from MovieLens 1M dataset
* README.md - these instructions
* corpus.py - creates corpus of documents (output becomes 'updatedCorpus.zip')
* mallet.csv - output of running Mallet LDA implementation on 'updatedCorpus.zip' with 100 topics (on July 24, 2020)
* ratings.csv - original 'ratings.csv' from MovieLens 1M data
* rbm100.csv - uses altered version of Microsoft's RBM implementation (https://github.com/microsoft/recommenders/blob/master/examples/00_quick_start/rbm_movielens.ipynb) which now outputs top 100 users for model only trained on 100 users; for comparison to our results
* rbmcontrol.py - compares our results (100 recommendations with LDA ran on 100 users v. altered Microsoft RBM implementation model on 100 users)
* **recommender.py** - handles creation of user profiles in currently commented out lines 24-99; output of this portion of algorithm stored as 'user_profiles.p' to avoid recalculating each time; then generates movie recommendations using collaborative filtering/neigborhood based reccommenders; outputs list of movie titles in English as recommendations for given userID (argv[1]) and uses 'k' for how many recommendations to output (argv[2]), and'n' number of neighbors to determine how large the neighborhood of users should be (argv[3])
* synthesizedMovieInfo.csv - .csv file associating movie titles, genres, plot summaries from Wikipedia dataset from Kaggle (https://www.kaggle.com/jrobischon/wikipedia-movie-plots) and movieIDs; used in 'corpus.py' to create original corpus; note: also uses  https://www.kaggle.com/danofer/movies-data-clean to fix issue of invalid name types from MovieLens 1M
* **movies.csv** - original .csv file from MovieLens 1M data; used in 'recommender.py' to convert recommended movieIDs to titles 
* topic-keys.txt - list of topic-keys from running Mallet LDA implementation with 100 topics (on July 24, 2020); converted to .txt to more easily parse; used in 'recommender.py' 
* updatedCorpus.zip - corpus of documents: contains 3123 movie documents of interest (those in both the Wikipedia dataset and MovieLens 1M dataset) containing genre and summary; created by 'corpus.py' using synthesizedMovieInfo.csv 
* **user_profiles.p** - Pickle file containing all user profiles created by 'recommender.py' (to avoid recalculating each time)

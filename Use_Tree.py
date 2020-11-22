''' This runs the classification algorithm for a given user '''

# hardiness - takes in climate number -> hardiness zone (str)
from API.Hardiness import hardiness_encoder
# climate - input zipcode -> climate category for tree (str)
from API.trewartha import translate_trewartha
# weather - input zipcode -> weather category for tree (int unless False)
from API.AzaveaClimate import weather_num

from Tree import build_tree, test, csv_wrangle

# Take in a zipcode

# take in each column of data of a dataset

# run them through the decision tree

# return the classification


def tree_from_zipcode(zipcode, sun, size, ptype, experience):

    # zipcode = user_value

    hardiness = hardiness_encoder(zipcode)
    climate = translate_trewartha(zipcode)
    weather = weather_num(zipcode)

    # Sun,Hardiness,Size,Climate,Weather,Type,Experience,Pack
    print(type(hardiness), type(climate), type(weather))

    user_profile = [sun, hardiness, size, climate, weather, type, experience]

    # build tree from dataset
    my_tree = build_tree(csv_wrangle('Datasets/Generate_20.csv'))

    # print tree
    print(my_tree)

    # classify the user
    test(user_profile)


if __name__ == "__main__":

    # Urbana IL 
    zipcode = '61801'
    sun = '1'
    size = '6'
    ptype = 'h'
    experience = '3' 

    tree_from_zipcode(zipcode, sun, size, ptype, experience)


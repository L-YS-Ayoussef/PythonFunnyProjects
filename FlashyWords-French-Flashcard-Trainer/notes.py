# notes --->

"""
** website for the words of each language (Frequency Lists). you can find it with the abbreviation of each language
-- the website --> [ Hermit Dave ]
** you can find these abbreviations on the website (google cloud-language support)
** after finding the words you can copy and paste them as a column in Excel, then you can translate the column in Excel
using this command for example ---> [ GOOGLETRANSLATE(text, "fr", "en") ] --> translating from French to English
** website for finding the words of each language selected by (top words for TV/Series) and other words ordered from
the more used to less
-- the website --> [ Wiktionary:Frequency lists ]
"""

"""
First, you convert the (DataFrame) after reading the [csv file] to a dictionary.
Then, you print this dictionary ---> printing the default form which is --->
{"french": {0: "the word"}}
** the default form --> {column: {index: value}}

** you can set the orient of the dictionary to ("records"), that the form will be like --->
[{column: value}] ---> for each column in the csv file there is an item in the dictionary inside the list
"""

"""
PhotoImage objects should not be created inside a function. Otherwise, it will not work.
"""

"""
creating a dataframe ---> converting the dataframe to a csv file 
--> to clear the index not to be shown in the csv file you can use [ index = False ]
[ data.to_csv("filename.csv", index=False) ]
"""













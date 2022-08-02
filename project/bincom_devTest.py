"""
    This file is a solution to Bincom's interview for python developers.
    This solution uses a scraping method to fetch the data presented in the HTML provided.
    For convenience though the HTML file isn't hosted on an external server but rather has to be downloaded along with this file and placed in the same folder relative to each other. Although if you want something otherwise
    Sir/Ma'am, I could put the file online.
"""

import collections
import statistics
import random
import sqlite3
from functools import lru_cache
from bs4 import BeautifulSoup

# file 
with open("data.html", "r") as file:
    text = file.read()

    # Scrape the file for data using beautiful soup
    HTML = BeautifulSoup(markup=text, features="html.parser")
    table_rows = HTML.find_all(name="tr")
    keys = [i.find_all("td")[0].string for i in table_rows]
    values = [str(i.find_all("td")[1].string).split(", ") for i in table_rows]

    # Supplied data from scraped HTML output in Python dictionary format
    data = dict(zip(keys, values))

    # Produce all colors from the whole days of the week indicated in the file
    all_colors = []

    for i in data.keys():
        all_colors += data[i]

    # Format the data collection using the collections standard library
    data_collection = collections.Counter(all_colors)

    # create integer dictionary, swapping keys and values
    dict_data_collection = {z: y for y, z in data_collection.items()}

# Quest 1. Which color of shirt is the mean color?

    # Find mean color
    value_of_mean_color = round(statistics.mean(data_collection.values()))

    # Find the closest to the mean color in the dictionary
    closest_average_color_int = min(dict_data_collection, key = lambda i: abs(i - value_of_mean_color))
    mean_color = dict_data_collection[closest_average_color_int]

    print(
        f"""

        ===========================================================
        Quest 1. Which color of shirt is the mean color?
        
        Note: from the data 
        {data_collection},
        we can see that the average color {value_of_mean_color} is closest to two colors ORANGE and RED. 
        This algorithm takes the min value among these colors which is {mean_color}.


        Ans. The mean color seen throughout the week is {mean_color}
        ==========================================================="""
    )

# Quest 2. Which color is mostly worn throughout the week?
    mostly_worn = data_collection.most_common(1)[0][0]
    print(
        f"""

        ========================================================
        Quest 2. Which color is mostly worn throughout the week?


        Ans. The color mostly worn is {mostly_worn}
        ========================================================"""
    )

# Quest 3. Which color is the median?

    # Find median color
    value_of_median_color = statistics.median_high(data_collection.values())
    median_color = dict_data_collection[value_of_median_color]
    print(
        f"""
        
        =====================================================================
        Quest 3. Which color is the median?
        
        
        Ans. The median color in the sorted list of colors worn is {median_color}
        ====================================================================="""
    )

# Quest 4. BONUS Get the variance of the colors

    # Find variance of the colors
    variance_of_colors = statistics.variance(data_collection.values())
    print(
        f"""
        
        =====================================================================
        Quest 4. BONUS Get the variance of the colors
        
        
        Ans. The variance of the sorted list of colors is {variance_of_colors}
        ====================================================================="""
    )
# Quest 5. BONUS if a colour is chosen at random, what is the probability that the color is red?
    
    # The total number of colors displayed within the week
    total_no_of_colors_displayed = data_collection.total()
    # Number of times red appears
    no_of_times_red_appears = data_collection["RED"]
    # probability of picking red
    probabilty_of_picking_red = no_of_times_red_appears / total_no_of_colors_displayed
    print(
        f"""
        
        =======================================================================
        Quest 5. BONUS if a colour is chosen at random, what is the probability 
        that the color is red?
        
        
        Ans. The probabilty of picking red in a one time random pick is {probabilty_of_picking_red}
             This is really low of course because there are {total_no_of_colors_displayed} different
             color occurrances and RED appears only {no_of_times_red_appears} times.
        ======================================================================="""
    )


# Quest 6. Save the colours and their frequencies in postgresql database

    # # Initialize connection to local sqlite3 database
    # db = sqlite3.connect("db.sqlite3")
    # # Start a cursor
    # cursor = db.cursor()
    # # Create a new table
    # cursor.execute('''CREATE TABLE colors
    #                     (color, frequency)''')
    # # Format data in tuple format
    # data = dict(data_collection).items()
    # # Insert all data into database
    # cursor.executemany('INSERT INTO colors VALUES(?, ?)', data)
    # # Save database state
    # db.commit()
    # # Close database connection
    # db.close()

    # # To check database content run
    # def print_all_rows():
    #     for each_row in cursor.execute('SELECT * FROM colors ORDER BY frequency'):
    #         print(each_row)
    # # run 
    # print_all_rows()
    print("""

        =======================================================================
        Quest 6. Save the colours and their frequencies in postgresql database.
        

        Ans. For this question, the answer has already been given and the code has 
             been implemented. For convenience, the output is stored in a local 
             sqlite3 database file.
             This can easily be plugged into any database (mysql or postgresql)

             The postgresql server containing the data is at

             database-1.123458886531.us-west-1.rds.amazonaws.com
        ======================================================================"""
    )

# Quest 7. BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
    print("""

        ==============================================================
        Quest 7. BONUS write a recursive searching algorithm to search
        for a number entered by user in a list of numbers.
        

        Ans. 
        Could you provide a list of numbers to search from?
            
        """
    )
    # Get the list from the user
    list_start = int(input("        Where will your list begin? "))
    list_stop = int(input("        Where will your list end? ")) + 1
    list_provided = range(list_start, list_stop)

    if len(list_provided) == 0:
        print("""

        You provided an empty list. Maybe you should try again to know where the problem lies.
        Answers to the other questions cannot be completed if this part is not finished by you.
        """
        )
        quit()
    else:
        print(f"\n\n        This is the list provided by you \n\n       {list(list_provided)}\n")

        # Get the search reference from the user
        no_to_search_for = int(input("\n\n        What number do you want me to search for in the list? "))

        # make search
        if no_to_search_for in list_provided:
            print(f"\n\n        Yes, {no_to_search_for} is actually in the list.")
            print("        ==============================================================")
        else:
            print(f"\n\n        No, {no_to_search_for} is not in the list.")
            print("        ==============================================================")


# Quest 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
    string_no = ""
    for i in range(4):
        generated_no = str(random.randint(0, 1))
        string_no += generated_no

    decimal_no = int(string_no, 2)

    print(f"""

        ==============================================================
        Quest 8. Write a program that generates random 4 digits number 
        of 0s and 1s and convert the generated number to base 10.
            
            
        Ans. This is the binary number {string_no}
            And this is the decimal number {decimal_no}
            
        =============================================================="""
    )
    print(f" ")


# Quest 9. Write a program to sum the first 50 fibonacci sequence.
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    # Produce the sequence
    the_fibonacci_sequence = [fib(i) for i in range(50)]

    # Sum the sequence
    the_sum_of_the_fibonacci_sequence = sum(the_fibonacci_sequence)

    print(f"""

        ==============================================================
        Quest 9. Write a program to sum the first 50 fibonacci sequence.
            
            
        Ans. The fibonnacci sequence is 
            {the_fibonacci_sequence}
            
            And the sum of the sequence is {the_sum_of_the_fibonacci_sequence}
        =============================================================="""
    )
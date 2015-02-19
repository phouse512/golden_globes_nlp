Usage Instructions
==================

To setup the environment, run:

	pip install -r requirements.txt

To run, type the following command:

	python gg.py <direct_path_to_json_file>

This will generate a to_be_graded.json file that you may use to run through the autograder.

To open the interface, open index.html

To run Fun Goal, type the following command:

    python getCelebSentiment.py <direct_path_to_json_file>
    
Libraries Used
-------------
Most of the heavy lifting from libraries came from our usage of the library scrapy, which gives a framework for us to scrape lots of awards and nominees quickly and easily.  We also used profilehooks to help us see which function calls were using up most of our resources, especially while optimizing our algorithm.

Future Usage
------------

Our system scales for future use by simply adding an additional spider/crawler with the new url and html structure to the scrapy library.  Outputting this to a JSON file will allow for our script to access it.  In future use, adding a dictionary of year to filenames would be helpful to scale as the number of years go by.

install packages
pip install -r requirements.txt

Then define the URLs (what we are testing against what) to visual_regression.py file. old_url is the original site and new_url is what we are testing.

 Tolerance level, how sensitive the comparison is, can be changed from compare_screenshots -file line 13.

run
python3 visual_regression.py

run time is around 1,5 hours. Make sure that device wont go to sleep while waiting.

If there are fails, those are in failed -folder. Number of the folder is just number from xml and not that important. Inside the numbered file should be two screenshots and .txt -file. Screenshots should be named Should_be and Is, Should_be.png is from original site and Is.png is from new site. Text file should include urls to the failed sites.

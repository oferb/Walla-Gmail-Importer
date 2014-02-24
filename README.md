Walla-Gmail-Importer
====================
### Converts www.walla.co.il contacts into a csv which can be imported to Gmail

Walla does not supply any export method for their contacts. Follow these steps to get the information directly from the browser:
  1. Change the website interface to the new one (new as of Feb. 2014).
  2. Go to the contacts page
  3. Copy-paste the contacts on the page into a txt file and save it
  4. Run the script as:

    python import_test.py txt_filename_including_path > gmail_contacts.txt


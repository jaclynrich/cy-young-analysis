## What sets Cy Young winners apart?
***


In this project, I investigate what sets Cy Young Award (CYA) winning pitchers apart from other starters and enable the comparison of the last ten years of winners to each other in a [Tableau](https://public.tableau.com/profile/jaclyn4031#!/vizhome/cy_young_pitchers_analysis_v2/CYYoungWinners) story.  I focused on how the winners compared with all other starters in the following areas:
  * Wins above replacement
  * Weighted runs saved
  * Longevity and consistency throughout the season
  * Quality of pitches
  * Quality of contact

### Data Gathering and Wrangling
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) was used for scraping.

*  Scraped PitchF/X data for starting pitchers from [Baseball Prospectus](https://legacy.baseballprospectus.com/pitchfx/leaderboards/) in scrape_pitchfx.py and saved in baseball_prospectus_pitchfx.csv
*  Scraped Cy Young Award data from [Baseball Reference](http://www.baseball-reference.com/awards) in scrape_cy_young.py and saved in cy_young_finalists.csv
* Downloaded pitching data from [Fangraphs](https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=10&type=8&season=2017&month=0&season1=2017&ind=0&team=0&rost=0&age=0&filter=&players=0)
  - Requested starting pitchers with at least 20 innings pitched
  - Did some basic cleaning in Excel - removed percents and any duplicate fields
  - Saved in 'fangraphs' sheet of starters_2008-2017.xlsx
* Downloaded Statcast data from [Baseball Savant](https://baseballsavant.mlb.com/statcast_search/)
  - Requested regular season starting pitchers with at least 200 pitches
  - Saved in 'statcast' sheet of starters_2008-2017.xlsx
* All data was joined together in joined_pitching_data_2008.py to make joined_pitching_data_2008.csv
* After calculated fields and parameters were added to the data set in Tableau, the final dataset was saved as joined_pitching_data_from_tableau.csv and as a Tableau data extract as joined_pitching_data_from_tableau.hyper
* Resources are included in resources.txt




For those unfamiliar with baseball, [Fangraphs'](https://www.fangraphs.com/library/pitching/complete-list-pitching/) glossary has explanations for most of the metrics and [MLB's](http://m.mlb.com/glossary/statcast/expected-woba) glossary has explanations for the Statcast fields.

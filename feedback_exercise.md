## Peer Feedback Exercise

* They think it would be interesting to see comparisons to the other newspapers that don't do a good job elaborating on the topic beyond just "air quality is bad"
* Are we taking into account wind data?
* Looking at data from 2018-2020 vs 2020-present because of people working at home (covid/early covid data)
* How would we format the data so that we can identify special events (like a winter inversion day) in our data set and have a drop down menu to select it?
* Topographic may not be the best background for the heat map
* They thought visual markers/landmarks would be helpful to orient readers to the map

## TA Feedback

One thing I don't think I saw mentioned in the data description is the geometries for TRAX lines and/or station locations---is that something that is publicly available? As a heads up, an annoying thing about using ZIP codes is that they sometimes change year-to-year and their boundaries aren't always well defined. To tackle that, the US Census keeps track of ZCTA codes instead, but they are usually different from USPS's ZIP codes: make sure your demographic data and geo data are merged on the same type of code. I like the design ideas and that you are incorporating multiple views; I'm wondering somewhat whether encoding the position along a TRAX line in a line chart is a very meaningful metric? (e.g., what do I glean from seeing how AQ changes as I take a train from campus to Daybreak). It probably depends on what the data looks like, but just something to keep in mind. Overall, great job and excited to see your project! Best, Max
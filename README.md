## Chicago's Top-10 Worst Ticket Collection Wards (2017)

This project does a quick pull of the City of Chicago's 2017 Parking Ticket data, summarized by ward.

Then uses python to join those features to a GeoJSON Ward map so I can present which wards have the worst proportion of "Paid" tickets, over the respective set of issued tickets for that ward. The map was made using [Felt](https://felt.com/about).

![Chicago's Top-10 Worst Ticket Collection Wards (2017)](https://github.com/BrendanMurnen/chicago-parking-tickets-2017/assets/47643845/8e620624-ddd4-4a7d-a089-f16c781f7e63)

### Datasets Used
* [City of Chicago Parking and Camera Ticket Data](https://www.propublica.org/datastore/dataset/chicago-parking-ticket-data), via ProPublica Data Store 
  * Uploaded to personal bigquery project and queried with `2017_ward_ticketing_stats.csv`
* [Boundaries - Wards (2015-2023)](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Wards-2015-2023-/sp34-6z76), via Chicago Data Portal
    * GeoJSON saved in Project as `Boundaries - Wards (2015-2023).geoJSON`

### Felt Visualization
https://felt.com/map/Chicagos-Top-10-Worst-Ticket-Collection-Wards-2017-raJta09BUR5aVConjo28MBB?loc=41.8552,-87.5456,10.81z&share=1 

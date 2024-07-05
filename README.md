# Aircraft Safety Analysis for Business Expansion

<img src="images/Flight-Safety-Instructions.jpg">

[Credit: Paxes.com](https://www.paxes.com/blog/flight-safety-instructions/)

## Introduction

This notebook contains an analysis aimed at identifying the safest aircraft models for a company expanding into operating airplanes for commercial and private use. The analysis is based on aircraft incident data from the NTSB up to 2023.

## Business Understanding

The goal of this analysis is to examine the risks associated with different aircraft makes and models and provide recommendations for the lowest-risk aircraft for purchase. The key questions include:
- Which aircraft models have the lowest occurrences of severe injuries from high-damage events?
- How do factors such as the number of engines and the purpose of flight impact the safety of the aircraft?

## Data Understanding

The dataset contains 90,348 entries and 31 columns, including:
- `Event.Id`: Unique identifier for each event.
- `Event.Date`: Date of the event.
- `Location`: Location of the event.
- `Country`: Country where the event occurred.
- `Injury.Severity`: Severity of injuries in the event.
- `Aircraft.damage`: Extent of damage to the aircraft.
- `Make` and `Model`: Manufacturer and model of the aircraft.
- `Number.of.Engines`: Number of engines on the aircraft.
- `Purpose.of.flight`: The purpose of the flight during the event.

## Limitations

- The dataset only contains information about flights that have gone wrong and does not include information about general safety, flight hours, maintenance, and successful flights. This presents an incomplete picture when attempting to determine overall aircraft safety.

## Data Preparation

The data preparation steps include:
1. Handling duplicate values.
2. Removing unnecessary columns and rows.
3. Handling missing values appropriately.
4. Converting columns to appropriate data types.
5. Feature engineering, such as encoding categorical values and extracting useful information from dates.

## Analysis and Findings

### Correlation Insights
- **Fatalities**:
    - The number of fatalities ranges from 0 to 228 with an average of 0.33 fatalities per incident.
    - The percentage of fatalities amongst total passengers per incident is 13.77% on average.
- **Correlation**:
    - Moderately positive correlation between both `Total.Uninjured` and `Total.Pax` with `Number.of.Engines`.
    - Weakly negative correlation between `Damage.Encoded` and `Total.Uninjured`.

### Damage Severity
- Private aircraft and helicopters have a more frequent instance of 'substantial' damage.
- Commercial aircraft have the highest instance of 'unknown' damage.

### Engine Types and Fatality Rates
- Turboprop engine types have the highest fatality rates in both private and commercial aircraft.
- Turboshaft engines account for the highest fatality rate in helicopters.

### Manufacturer Insights
- **Cessna**:
    - Cessna has one of the lower fatality rates for private aircraft but the highest incident rate.
    - Models like C-150, Centurion, Skyhawk, Skylane, and Skywagon all have over 200 records and < 20% fatality rate (except for the Centurion model with a 21% fatality rate).
- **Non-Cessna Private Craft**:
    - Bombardier Challenger 600 and Embraer EMB-145 show promising safety records with a 0% mean fatality rate.
- **Commercial Aircraft**:
    - All Airbus, Boeing, and Embraer models generally have a strong safety record, except Boeing 707 and 767.
    - Mitsubishi models, particularly the MU-2 series, show high fatality rates.
- **Helicopters**:
    - The Bell 206, Robinson R-22, and Robinson R-44 have < 20% mean fatality rate.

## Recommendations

Based on the analysis, here are some recommendations for safer aircraft choices:

### Private Aircraft

- Single-engine aircraft tend to have the lowest average fatality rates.
- Exercise caution with turboprop engines, which have the highest fatality rates. Turbofan and reciprocating engines have nearly tied for the lowest fatality rates.
- Generally, more passengers equate to lower fatality rates.

### Commercial Aircraft

- Dual-engine aircraft have the highest fatality rates but still lower than all private aircraft engine counts.
- Turboprop engines have the highest fatality rates by a significant margin, while turbofan and turbojet engines have the lowest fatality rates.
- Higher passenger counts generally correlate with lower fatality rates.

### Helicopters

- Turboshaft engine types have the highest fatality rates, and reciprocating engines have the lowest, though both have relatively low rates.
- There is no apparent correlation between passenger count and fatality rate, which makes sense since helicopters aren't typically capable of carrying large numbers of people.
## Additional Considerations

- The recommendations can become more accurate and helpful upon further review from the relevant stakeholders within the business. Important factors to consider include:
  - Are we focusing on passenger aircraft, cargo aircraft, or both?
  - Are we interested in larger long-haul flights or shorter hops?
  - Are helicopters of interest?
  - Are we looking for business jets to carry C-suite executives to meetings?
  - Do we need smaller short-runway capable aircraft to carry medications or other supplies to remote locations?

## Conclusion

This analysis provides insights into the safety of different aircraft models and makes actionable recommendations to support the company's expansion into aircraft operations. The findings are based on detailed analysis and are aimed at minimizing risks associated with aircraft selection.

## Acknowledgments

- Data sourced from the National Transportation Safety Board (NTSB).
- Aircraft sales information sourced from Assets America and General Aviation News.

---

For more details, please refer to the Jupyter Notebook included in this repository.
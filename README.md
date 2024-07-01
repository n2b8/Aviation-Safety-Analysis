# Aircraft Safety Analysis for Business Expansion

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
    - Models like C-150, Centurion, Skyhawk, Skylane, and Skywagon all have over 200 records and < 20% fatality rate.
- **Non-Cessna Private Craft**:
    - Bombardier Challenger 600 and Embraer EMB-145 show promising safety records with a 0% mean fatality rate.
- **Commercial Aircraft**:
    - All Airbus, Boeing, and Embraer models generally have a strong safety record, except Boeing 737 and 767.
    - Mitsubishi models, particularly the MU-2 series, show high fatality rates.
- **Helicopters**:
    - The Bell 206, Robinson R-22, and Robinson R-44 have < 20% mean fatality rate.

## Recommendations

Based on the analysis, the following recommendations are made for safer aircraft choices:

### Private Aircraft
- Consider Cessna models like C-150, Centurion, Skyhawk, Skylane, and Skywagon for their lower fatality rates.
- Bombardier Challenger 600 and Embraer EMB-145 show promising safety records with a 0% mean fatality rate.

### Commercial Aircraft
- Airbus, Boeing, and Embraer models generally have a strong safety record. However, caution should be exercised with the Boeing 767 due to its higher mean fatality rate.
- Mitsubishi models, particularly the MU-2 series, show high fatality rates and should be approached with caution.

### Helicopters
- The Bell 206, Robinson R-22, and Robinson R-44 are recommended for their lower fatality rates and higher number of incidents, indicating a robust dataset.

## Conclusion

This analysis provides insights into the safety of different aircraft models and makes actionable recommendations to support the company's expansion into aircraft operations. The findings are based on detailed analysis and are aimed at minimizing risks associated with aircraft selection.

## Acknowledgments

Data sourced from the National Transportation Safety Board (NTSB).

---

For more details, please refer to the Jupyter Notebook included in this repository.
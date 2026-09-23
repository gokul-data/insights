# Gokul's Data Signal 08 — sources and method

## Controlling source

- International Energy Agency, *Key Questions on Energy and AI*, published 16 April 2026: https://www.iea.org/reports/key-questions-on-energy-and-ai
- Executive summary: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

## Supporting source

- International Energy Agency, *Electricity 2026*: https://www.iea.org/reports/electricity-2026

## Calculations

- 2025–2030 growth = `(950 / 485) - 1` = 95.9%, displayed as 96%.
- Five-year compound annual growth = `(950 / 485)^(1/5) - 1` = 14.4%.
- Site electricity = selected MW × 8,760 hours ÷ 1,000,000 = annual TWh at continuous full load. This is a capacity-envelope calculation, not a forecast of actual consumption.
- IEA describes AI-focused data-centre electricity use as approximately tripling from 2025 to 2030. The dashboard indexes 2025 to 100 and 2030 to 300 solely to show that relative change.
- IEA states AI server power density increased 11-fold from 2020 to 2025 and is set to rise a further fourfold by 2027. The dashboard therefore uses an index of 1, 11 and 44. This is an index, not watts per rack.

## Interpretation boundary

The 2030 figures are projections, not observed outcomes. National shares refer to data centres' contribution to total electricity-demand growth, not their share of total electricity consumption. “Almost half”, “more than half” and “up to one-fifth” are intentionally shown as approximate thresholds.

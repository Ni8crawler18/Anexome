# Annexome

A data-driven Streamlit application for analyzing India's cultural tourism patterns and traditional art forms.
([text](https://anexome.streamlit.app/))

## Overview

Annexome processes government and tourism datasets to identify underrepresented cultural assets and visualize heritage-based tourism trends. The platform integrates data from data.gov.in and related sources to support sustainable tourism development.

## Architecture

- **Frontend**: Streamlit (Python)
- **Backend**: Snowflake (cloud data warehouse)
- **Data Sources**: Government tourism schemes, cultural investments, GIS location data, seasonal travel patterns

## Features

- **Interactive Maps**: Cultural hotspots with filtering capabilities
- **Analytics Dashboard**: Tourism trends and heritage investment tracking
- **Art Form Database**: Regional art forms linked to geographical data
- **Destination Insights**: Data-driven identification of untapped cultural destinations
- **Policy Analysis**: Impact assessment of government heritage schemes

## Data Pipeline

1. Ingestion from government APIs and datasets
2. Processing and transformation in Snowflake
3. Real-time visualization through Streamlit interface
4. Interactive filtering and analysis tools

## Use Cases

- Tourism pattern analysis and forecasting
- Cultural heritage preservation planning
- Sustainable tourism route optimization
- Government policy impact assessment

## Installation

```bash
pip install streamlit snowflake-connector-python
streamlit run app.py
```

## Configuration

Configure Snowflake connection parameters in `config.yaml`:

```yaml
snowflake:
  account: your_account
  user: your_user
  password: your_password
  warehouse: your_warehouse
  database: your_database
```
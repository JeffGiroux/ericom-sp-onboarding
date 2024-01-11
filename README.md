# Ericom Service Provider Onboarding

## To Do -- WORK IN PROGRESS
1. initial repository
2. identify necessary API calls

## Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This code will automate Service Provider onboarding for [Ericom Security](https://www.ericom.com). The API endpoints for Ericom will be called to setup the tenant and filtering policies. 


## Requirements

- Access to ZTAdmin portal
- Ericom Security API key
- Python3

```
git clone https://github.com/JeffGiroux/ericom-sp-onboarding.git
cd ericom-sp-onboarding
pip3 install -r requirements.txt
```

## Usage

### Onboarding

1. TBD - Update variables

2. Execute python command.

Syntax:
```
python3 sp_onboard.py <Tenant ID> <API Key>
```

Example:
```
python3 sp_onboard.py 555-444-333-222-111 keyAAABBBCCC

Authenticating and retrieving token...
TBD...status "tenant onboarded"
Done!
```

3. View results

TBD - validate tenant and policies in Ericom.


### Decommissioning

1. TBD - Update variables

2. Execute python command.

Syntax:
```
python3 sp_decommission.py <Tenant ID> <API Key>
```

Example:
```
python3 sp_decommission.py 555-444-333-222-111 keyAAABBBCCC

Authenticating and retrieving token...
TBD...status "tenant decommed"
Done!
```

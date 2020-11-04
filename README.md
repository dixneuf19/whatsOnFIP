# What's on FIP ?

[![Test](https://github.com/dixneuf19/whatsOnFIP/workflows/Test/badge.svg)](https://github.com/dixneuf19/whatsOnFIP/actions?query=workflow%3ATest) [![Build and release](https://github.com/dixneuf19/whatsOnFIP/workflows/Build%20and%20release/badge.svg)](https://github.com/dixneuf19/whatsOnFIP/actions?query=workflow%3A"Build+and+release") [![CodeQL](https://github.com/dixneuf19/whatsOnFIP/workflows/CodeQL/badge.svg)](https://github.com/dixneuf19/whatsOnFIP/actions?query=workflow%3ACodeQL)

## Local development

You can build the *Docker* image with `make build` and then run it with `make run`.

The app is available at <http://localhost:8000>.

## Create k8s secret

Add your RADIO_FRANCE_API_TOKEN token into your `.env` file for development (**don't commit this file**).

Then you can create the secret with `kubectl create secret generic radio-france-api-token --from-env-file=.env`.

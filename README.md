# What's on FIP ?

[![Deploy](https://github.com/dixneuf19/whatsOnFIP/workflows/Deploy/badge.svg)](https://github.com/dixneuf19/whatsOnFIP/actions?query=workflow%3ADeploy)

## Local development

You can build the *Docker* image with `make build` and then run it with `make run`.

The app is available at <http://localhost:8000>.

## Create k8s secret

Add your RADIO_FRANCE_API_TOKEN token into your `.env` file for development (**don't commit this file**).

Then you can create the secret with `kubectl create secret generic radio-france-api-token --from-env-file=.env`.

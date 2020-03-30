#!/usr/bin/env bash

docker build -t gcr.io/varsha-project/sentimentclassifier:v1 .

docker run -it -p 8080:8080 gcr.io/varsha-project/sentimentclassifier:v1
#!/bin/bash


# docker run --rm \
#     -v $PWD:/local openapitools/openapi-generator-cli generate \
#     -i /local/openapi.json \
#     -g python \
#     -o /local/out/python
                
docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i /local/openapi.json \
    -g typescript \
    -o /local/out/ts
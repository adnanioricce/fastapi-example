#!/bin/bash

health=$(curl http://localhost:8001/health)

printf $"\nhealth: ${health}\n"

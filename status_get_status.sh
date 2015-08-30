#!/bin/bash

DIR=MC1/
multicrab -status -c ${DIR}
multicrab -get -c ${DIR}
multicrab -status -c ${DIR}

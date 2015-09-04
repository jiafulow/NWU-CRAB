#!/bin/bash

DIR=MC2/
multicrab -status -c ${DIR}
multicrab -get -c ${DIR}
multicrab -status -c ${DIR}

#DIR=MC1/ZZ/
#crab -status -c ${DIR}
#crab -get -c ${DIR}
#crab -status -c ${DIR}

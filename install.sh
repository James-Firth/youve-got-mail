#!/bin/bash

# Generic variables
working_dir=$(pwd -P)
parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$parent_path"
project_root=$(git rev-parse --show-toplevel || echo ".")
#end Generic variables

virtualenv ygm
source "$parent_path/ygm/bin/activate"
pip install --upgrade pip

cd "$parent_path"
pip install -r requirements.txt

cd "$working_dir"

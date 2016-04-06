#!/bin/sh

arch=$(uname -m)
node_version=node-v4.4.2-linux-$arch.tar.gz
if [ ! -e $node_version ];
then
    echo "We are downloading Node.js"
    curl -L https://nodejs.org/dist/v4.4.2/$node_version \
    > $node_version
fi

if [ ! -e node ];
then
    mkdir -p node
    echo "Decompressing Node.js"
    tar -xvf $node_version --strip-components=1 -C ./node/
    echo "Node.js is ready."
fi

if [ ! -e ./node/lib/node_modules/bower/bin/bower ];
then
    echo "Using Node.js to install bower for client-side dependencies."
    ./node/bin/npm install -g bower
    echo "Bower has been installed"
fi

echo "Using Bower to install client-side dependencies"
./node/lib/node_modules/bower/bin/bower install

echo "You are now ready to run add_stations.sh or python app.py"


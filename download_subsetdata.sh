#!/usr/bin/env bash

wget http://labrosa.ee.columbia.edu/~dpwe/tmp/millionsongsubset.tar.gz
wait
tar xvzf millionsongssubset_full.tar.gz
wait 
rm millionsongssubset_full.tar.gz

cd MillionSongSubset

wget http://labrosa.ee.columbia.edu/millionsong/sites/default/files/lastfm/lastfm_subset.zip
unzip lastfm_subset.zip
rm lastfm_subset.zip

cd ..

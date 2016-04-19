#!/usr/bin/env bash
file="notes.sqlite3.db"
if [ -r $file ] ; 
    then
        echo "Removing $file"
        rm $file;
fi

sqlite3 $file < setup.sql 

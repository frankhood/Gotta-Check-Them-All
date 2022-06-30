#!/usr/bin/env bash

ENV_FILE=.env

get_random_password(){
    head -c 1024 /dev/urandom | base64 | tr -cd "[:upper:][:digit:]" | head -c 32
}
get_random_string(){
    od -x /dev/urandom | head -1 | awk '{OFS="_"; print $2$3,$4,$5,$6,$7$8$9}'
}

if [[ -f "$ENV_FILE" ]]; then
    echo ".env already exists!"
else
    cp .env_template .env
    
    if [[ "$ENV_STARTFH_DB_MYSQL_ROOT_PWD" ]]; then
        sed -i -e "s/__DATABASE_ROOT_PASSWORD__/$ENV_STARTFH_DB_MYSQL_ROOT_PWD/g" ./.env
    else
        sed -i -e "s/__DATABASE_ROOT_PASSWORD__/$(get_random_password)/g" ./.env
    fi

    if [[ "$ENV_STARTFH_DB_PWD" ]]; then
        sed -i -e "s/__DATABASE_PASSWORD__/$ENV_STARTFH_DB_PWD/g" ./.env
    else
        sed -i -e "s/__DATABASE_PASSWORD__/$(get_random_password)/g" ./.env
    fi

    sed -i -e "s/__SECRETKEY__/$(get_random_password)/g" ./.env

    if [ -f ./.env-e ]
    then
        rm ./.env-e
    fi
fi

base_url="http://localhost:8000/api"
upload_init_url="${base_url}/upload"
token_url="${base_url}/token"
username="admin"
password="admin"

access_token=$(
    curl ${token_url} --silent --data "username=${username}" --data "password=${password}" \
        | cut --delimiter=: --fields=2 \
        | tr --delete '\"}'
)

filename=$(basename $1)
content_type=$(
    file --mime-type $1 \
        | cut --delimiter=\  --fields=2 \
        | tr --delete ';'
)
echo "Uploading ${filename} (${content_type})"

upload_url=$(
    curl $upload_init_url --dump-header - --silent --header "Authorization: Token $access_token" --data "title=$filename" \
        | grep Location \
        | cut --delimiter=\  --fields=2 \
        | tr --delete '[[:space:]]'
)

curl "$upload_url" --silent --request PUT --header "Content-Type:$content_type" --data-binary @${1} 

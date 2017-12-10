#! /bin/bash
CONTENTPATH="/Users/marianna/Documents/Projects/blog/content/"

TEXT="Here are the slides."
TAGS="talks, slides"
CATEGORY="General"
DATE=`date +%Y-%m-%d`

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -t|--title)
    TITLE="$2"
    shift # past argument
    shift # past value
    ;;
    -x|--text)
    TEXT="$2"
    shift # past argument
    shift # past value
    ;;
    -s|--slides)
    SLIDEFILE="$2"
    shift # past argument
    shift # past value
    ;;
    -a|--tags)
    TAGS="$2"
    shift # past argument
    shift # past value
    ;;
    -c|--category)
    CATEGORY="$2"
    shift # past argument
    shift # past value
    ;;
esac
done
set -- "${POSITIONAL[@]}"

if [ -n "$TITLE" ] && [ -n "$SLIDEFILE" ]; then 

    FILENAME=$CONTENTPATH"pages/"$(echo $TITLE | sed 's/ /_/g').md
    echo "Title: "$TITLE > $FILENAME
    echo "Date: "$DATE >> $FILENAME
    echo "Tags: "$TAGS >> $FILENAME
    echo "Category: "${CATEGORY}$'\n' >> $FILENAME
    echo "[$TEXT]({filename}${SLIDEFILE})" >> $FILENAME

    pelican content/
    ghp-import output/
    git push origin gh-pages

else
    echo "Title and slide path are both required."
fi

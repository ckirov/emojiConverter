emojiConverter
==============

Simple script to convert between different emoji encodings.

You'll need the conversion table from http://punchdrunker.github.io/iOSEmoji/table_html/ios6/emoji_ios6.json in the same directory as the script.

The file isn't valid json, but the following substitution will fix that:

```
sed -i .bak 's/,}/}/g' emoji_ios6.json
```

Then, run the script as follows:

```
python emojiConverter.py inCoding outCoding inFile outFile
```

*inCoding* and *outCoding* specify the enccoding of the input file and desired encoding of the output file. Possible values are *utf8*, *docomo-utf8*, *softbank-utf8*, and *kddi-utf8*.


*inFile* and *outFile* specify paths to the input file and the desired output file.

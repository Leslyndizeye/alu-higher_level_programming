#!/bin/bash
# Compile the Python script and save it as $PYFILEc
python3 -m compileall -b -x "__pycache__" "$PYFILE"

# Check if the compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful."
    compiled_file="${PYFILE}c"
    if [ -e "$compiled_file" ]; then
        mv "$PYFILE" "$compiled_file"
    else
        $PYFILE
    fi
else
    $PYFILE
fi

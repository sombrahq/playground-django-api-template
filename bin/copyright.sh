#!/usr/bin/env bash

ok=0
copyright=$(<./legal/copyright.txt)

while read -r fn; do
  echo "Fixing: ${fn}";
  printf  '%s\n' "${copyright}" | cat - "${fn}" > temp && mv temp "${fn}"
  ok=1;
done < <(grep -rL -i -E "^# Copyright \(c\) .* - All rights reserved\.$" --include "*.py" .)

exit ${ok}

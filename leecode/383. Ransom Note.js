function canConstruct(noteText, magazineText) {
  const noteArray = [...noteText];
  const magazineArray = [...magazineText];
  const magazineObject = {};

  magazineArray.forEach((word) => {
    if (!magazineObject[word]) magazineObject[word] = 0;
    magazineObject[word]++;
  });

  const noteIsPossible = noteArray.every((word) => {
    if (!magazineObject[word]) {
      return false;
    }
    magazineObject[word]--;
    return magazineObject[word] >= 0;
  });

  return noteIsPossible;
}

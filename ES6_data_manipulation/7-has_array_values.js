function hasValuesFromArray(set, array) {
  const checks = array.every((item) => set.has(item));
  return checks;
}

export default hasValuesFromArray;

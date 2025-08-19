export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (const [idx, value] of array.entries()) {
    result[idx] = appendString + value;
  }

  return result;
}

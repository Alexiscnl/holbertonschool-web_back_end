export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (const value of array) {
    result.push(appendString + value);
  }

  return result;
}

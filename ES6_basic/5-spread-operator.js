export default function concatArrays(array1, array2, string) {
  const concact = [...array1, ...array2, ...string];
  return concact;
}

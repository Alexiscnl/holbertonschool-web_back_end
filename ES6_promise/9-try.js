export default function guardrail(mathFunction) {
  const qeue = [];

  try {
    const result = mathFunction();
    qeue.push(result);
  } catch (e) {
    qeue.push(String(e));
  } finally {
    qeue.push('Guardrail was processed');
  }
  return qeue;
}

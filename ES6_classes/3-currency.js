export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  set code(newcode) {
    if (typeof newcode !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._code = newcode;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

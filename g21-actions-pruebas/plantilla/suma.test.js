const test = require('node:test');
const assert = require('node:assert');
const { suma } = require('./suma.js');

test('suma dos números', () => {
  assert.strictEqual(suma(2, 3), 5);
});

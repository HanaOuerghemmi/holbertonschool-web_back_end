var chai = require('chai');

const calculateNumber = require('./2-calcul_chai');

const SUM = 'SUM';
const SUBTRACT = 'SUBTRACT';
const DIVIDE = 'DIVIDE';
const INVALID = 'INVALID';

describe('calculateNumber', function () {
  describe('SUM no Round', function () {
    it('should return 5', function () {
      chai.expect(calculateNumber('SUM', 1, 4)).to.equal(5);
    });
  });

});
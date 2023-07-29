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
  describe('SUBTRACT', function () {
    it('should return 2', function () {
      chai.expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
    });
  });
  describe('DIVIDE', function () {
    it('should return 2', function () {
      chai.expect(calculateNumber('DIVIDE', 8, 4)).to.equal(2);
    });
  });
  describe('DIVIDE Error', function () {
    it('should return Error', function () {
      chai.expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });
});